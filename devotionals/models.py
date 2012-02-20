from django.db import models

class Devotional(models.Model):
    "Model that represents devotionals"

    title = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateTimeField('created date')

    def __str__(self):
        return self.title
