Django widgets for replacing textareas with CodeMirror, an in-browser code editor.
Tested on Django 1.6+, support Python 2.7 and Python 3.4+.

.. image:: https://travis-ci.org/sk1p/django-codemirror2.svg?branch=master
    :target: https://travis-ci.org/sk1p/django-codemirror2


Installing
==========

1. run ``pip install django-codemirror2``
2. Add ``codemirror2`` to INSTALLED_APPS
3. Collect static files: ``python manage.py collectstatic``

To use django-codemirror2 directly from git, you need to initialize
the Codemirror submodule by running ``git submodule init && git submodule update``.


Usage
=====

::

    from django import forms
    from codemirror2.widgets import CodeMirrorEditor

    class TestForm(forms.Form):
        css = forms.Charfield(widget=CodeMirrorEditor(options={'mode': 'css'}))

The ``options`` argument will be passed as JSON to ``CodeMirror.fromTextArea``, see
http://codemirror.net/manual.html#config for possible values. Do not pass user-controlled
data as options, as this can lead to an XSS vulnerability.

If you want to use a mode that depends on other modes, for example ``htmlmixed``, you
need to load the dependencies, too, by passing the ``modes`` parameter:

::

    html = forms.Charfield(widget=CodeMirrorEditor(modes=['css', 'xml', 'javascript', 'htmlmixed'],
                options={'mode': 'htmlmixed'}))

If you want to customize the Javascript used to initialize the CodeMirror editor, use ``script_template``::

    foo = forms.Charfield(widget=CodeMirrorEditor(options={'mode': 'xml'}, 
                script_template='some/template.html'))

You can base your script template on the included template ``codemirror_script.html``.


Example app
===========

There is a simple example app included. To run it:

1. run ``tox -e devenv``
2. run ``./run_example_server.sh``
3. visit http://localhost:8000/admin/testapp/ in your browser.
