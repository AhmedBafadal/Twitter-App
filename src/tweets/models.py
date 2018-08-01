from django.db import models

# Create your models here.
class Tweet(models.Model):
    
    # Content of tweet (restricted to 140 chars)
    content = models.CharField(max_length=140)

    # Timestamp of update to tweet
    updated = models.DateTimeField(auto_now=True)
    
    # Timestamp of tweet
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    