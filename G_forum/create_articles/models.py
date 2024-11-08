from django.db import models

# Create your models here.


class SaveArticles(models.Model):
    heading = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)