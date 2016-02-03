from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class TestCss(models.Model):
    title = models.CharField(max_length=255)
    css = models.TextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TestHTML(models.Model):
    title = models.CharField(max_length=255)
    html = models.TextField()

    def __str__(self):
        return self.title
