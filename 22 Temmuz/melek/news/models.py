from django.db import models

# Create your models here.

#pascal case?
class NewsItem(models.Model):
    title = models.CharField(max_length=201)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
