from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

BASE_DIR = os.path.dirname(__file__)

def read(fname):
    return open(os.path.join(BASE_DIR, fname)).read()

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

data_files = []
for dirpath, dirnames, filenames in os.walk(os.path.join(BASE_DIR, "codemirror2", "static")):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

README = read("README.rst")

setup(name="django-codemirror2",
    version="0.0.3",
    author_email="alex@gc-web.de",
    author="Alexander Clausen",
    description="Django widgets for replacing textareas with CodeMirror2, an in-browser code editor",
    url="https://github.com/sk1p/django-codemirror2",
    long_description=README,
    packages=["codemirror2"],
    package_data = {'codemirror2': [os.path.join("templates", "codemirror2", "*")]},
    data_files=data_files,
    include_package_data=True,
)
