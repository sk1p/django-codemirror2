from setuptools import setup
import os

BASE_DIR = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(BASE_DIR, fname)).read()

README = read("README.rst")

setup(
    name="django-codemirror2",
    version="0.1.3",
    author_email="alex@gc-web.de",
    author="Alexander Clausen",
    url="https://github.com/sk1p/django-codemirror2",
    description="Django widgets for replacing textareas with CodeMirror2,"
                " an in-browser code editor",
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Text Editors',
    ],
    include_package_data=True,
    packages=[
        "codemirror2",
        "codemirror2.tests",
    ],
)
