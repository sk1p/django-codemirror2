from itertools import chain
from django.contrib.staticfiles.finders import find
import pytest
from codemirror2.widgets import CodeMirrorEditor


@pytest.fixture
def w():
    """
    construct a CodeMirrorEditor widget with default settings
    """
    return CodeMirrorEditor()


def test_dont_share_options(settings):
    settings.CODEMIRROR_DEFAULT_OPTIONS = {"default": "option"}
    w1 = CodeMirrorEditor(options={"w1": "opt1"})
    w2 = CodeMirrorEditor(options={"w2": "opt2"})

    assert w1.options != w2.options
    assert w1.options == {"w1": "opt1", "default": "option"}
    assert w2.options == {"w2": "opt2", "default": "option"}


def test_mode_populated_from_options():
    w = CodeMirrorEditor(options={"mode": "python"})
    assert w.modes == ["python"]


def test_mode_populated_w_modelist(w):
    assert len(w.modes) == 16


def test_pass_modes():
    modes = ["python", "css", "xml", "javascript", "htmlmixed"]
    w = CodeMirrorEditor(options={"mode": "python"},
                         modes=modes)
    assert w.modes == modes
    assert w.options == {"mode": "python"}


def test_default_theme(w):
    assert w.themes == ["default"]


def test_themes_populated_from_options():
    w = CodeMirrorEditor(options={"theme": "dark"})
    assert w.themes == ["dark"]


def test_themes_populated_from_args():
    themes = ["light", "dark", "default"]
    w = CodeMirrorEditor(themes=themes)
    assert w.themes == themes


def test_render_widget(w):
    html = w.render("code", "")
    assert 'name="code"' in html
    assert 'document.getElementById("id_code")' in html


def test_media_w_mode():
    w = CodeMirrorEditor(options={"mode": "python"})
    js, css = w.media._js, w.media._css
    assert js == [
        "codemirror2/lib/codemirror.js",
        "codemirror2/addon/mode/overlay.js",
        "codemirror2/mode/python/python.js",
    ]
    assert css == {
        "screen": [
            "codemirror2/lib/codemirror.css"
        ]
    }
    for f in chain(js, css["screen"]):
        assert find(f)


def test_mode_extra_css():
    w = CodeMirrorEditor(options={"mode": "tiki"})
    js, css = w.media._js, w.media._css
    assert "codemirror2/mode/tiki/tiki.css" in css["screen"]
    for f in chain(js, css["screen"]):
        assert find(f)


def test_staticfiles_exist():
    """
    in default configuration (with "all" modes), the static files should exist
    """
    w = CodeMirrorEditor()
    js, css = w.media._js, w.media._css
    for f in chain(js, css["screen"]):
        assert find(f)
