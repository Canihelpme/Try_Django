from django.db import models
from django.urls import reverse

class reporter(models.Model):
    fullname = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname


class article(models.Model):
    headline = models.CharField(max_length=200)
    contents = models.TextField()
    reporter = models.ForeignKey(reporter, on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return self.headline
    