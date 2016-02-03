from setuptools import setup

setup(
    name="django-codemirror2",
    version="0.2",
    author_email="alex@gc-web.de",
    author="Alexander Clausen",
    url="https://github.com/sk1p/django-codemirror2",
    description="Django widgets for replacing textareas with CodeMirror2,"
                " an in-browser code editor",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: JavaScript',
        'Topic :: Text Editors',
    ],
    include_package_data=True,
    packages=[
        "codemirror2",
        "codemirror2.tests",
    ],
)
