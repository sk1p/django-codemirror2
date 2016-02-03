# -*- encoding: utf-8 -*-
from django.forms import widgets
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
import json
import copy
from django.contrib.admin import widgets as admin_widgets


class CodeMirrorEditor(widgets.Textarea):
    def __init__(self, modes=None, themes=None, options=None,
                 script_template="codemirror2/codemirror_script.html", *args, **kwargs):
        """
        options: will be json-encoded and passed to ``CodeMirror.fromTextArea``

        modes: list of mode files to load, example: ["xml", "css", "python"].

        themes: list of themes to load, example: ["default", "neat", "elegant", "night"]
        """
        super(CodeMirrorEditor, self).__init__(*args, **kwargs)
        def_options = copy.deepcopy(getattr(settings, "CODEMIRROR_DEFAULT_OPTIONS", {}))
        if options is not None:
            def_options.update(options)
        self.options = def_options
        if modes is None:
            if 'mode' in self.options:
                modes = [self.options['mode']]
            else:
                modes = ["clike", "diff", "htmlmixed", "lua", "sql", "rst", "smalltalk", "xml",
                        "css", "haskell", "javascript", "php", "python", "scheme", "stex", "yaml"]
        self.modes = modes
        if themes is None:
            if 'theme' in self.options:
                themes = [self.options['theme']]
            else:
                themes = ["default"]
        self.themes = themes
        self.script_template = script_template

    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(CodeMirrorEditor, self).render(name, value, attrs, **kwargs)
        context = {
            'name': name,
            'options': json.dumps(self.options),
        }
        return rendered + mark_safe(
            render_to_string(self.script_template, context)
        )

    @property
    def media(self):
        js_files = ["codemirror2/lib/codemirror.js"]
        js_files += ["codemirror2/addon/mode/overlay.js"]
        js_files += [("codemirror2/mode/%s/%s.js" % (mode, mode)) for mode in self.modes]
        css_files = ["codemirror2/lib/codemirror.css"]
        css_files += [("codemirror2/theme/%s.css" % theme) for theme in self.themes
                      if theme != "default"]  # default theme is included in codemirror.css
        # some modes have extra css files, too:
        # TODO: autodetect
        need_css = ["tiki", "tiddlywiki"]
        for mode in need_css:
            if mode in self.modes:
                css_files.append("codemirror2/mode/%s/%s.css" % (mode, mode))
        return widgets.Media(js=js_files, css={'screen': css_files})


class AdminCodeMirrorEditor(CodeMirrorEditor, admin_widgets.AdminTextareaWidget):
    pass
