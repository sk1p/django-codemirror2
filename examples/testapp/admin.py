from django.contrib import admin
from codemirror2.widgets import CodeMirrorEditor
from testapp.models import TestCss, TestHTML


class TestCssAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "css":
            kwargs["widget"] = CodeMirrorEditor(
                options={"mode": "css", "lineNumbers": True}
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


class TestHTMLAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "html":
            kwargs["widget"] = CodeMirrorEditor(
                options={"mode": "htmlmixed", "lineNumbers": True},
                modes=["css", "xml", "javascript", "htmlmixed"],
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(TestCss, TestCssAdmin)
admin.site.register(TestHTML, TestHTMLAdmin)
