from django.db import models


class TestCss(models.Model):
    title = models.CharField(max_length=255)
    css = models.TextField()

    def __str__(self):
        return self.title


class TestHTML(models.Model):
    title = models.CharField(max_length=255)
    html = models.TextField()

    def __str__(self):
        return self.title
