def pytest_configure():
    from django.conf import settings

    settings.configure(
        SECRET_KEY="nope",
        STATIC_URL="/static/",
        INSTALLED_APPS=[
            "codemirror2",
        ],
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
            },
        ],
    )
