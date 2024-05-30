from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    image = models.URLField(null=True, blank=True)
    source = models.CharField(max_length=100, default='N/A')
    
    def __str__(self):
        return self.title
