from django.db import models

# Create your models here.
class Topic(models.Model):
    """the topic for users"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the string form of the model"""
        return self.text
