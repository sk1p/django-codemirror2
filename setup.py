from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read("README.rst")

setup(name="django-codemirror2",
    version="0.0.2",
    author_email="alex@gc-web.de",
    author="Alexander Clausen",
    description="Django widgets for replacing textareas with CodeMirror2, an in-browser code editor",
    url="https://github.com/sk1p/django-codemirror2",
    long_description=README,
    packages=["codemirror2"],
    package_data = {'codemirror2': [os.path.join("templates", "codemirror2", "*")]},
)
