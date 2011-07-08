# -*- encoding: utf-8 -*-
from django.contrib import admin
from codemirror2.widgets import CodeMirrorEditor
from testapp.models import TestCss, TestHTML

class TestCssAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "css":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'css'})
        return super(TestCssAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class TestHTMLAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "html":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'htmlmixed'}, modes=['css', 'xml', 'javascript', 'htmlmixed'])
        return super(TestHTMLAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(TestCss, TestCssAdmin)
admin.site.register(TestHTML, TestHTMLAdmin)
