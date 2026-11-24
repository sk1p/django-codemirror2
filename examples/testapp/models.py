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


class TestParent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TestChild(models.Model):
    html = models.TextField()
    parent = models.ForeignKey(TestParent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
