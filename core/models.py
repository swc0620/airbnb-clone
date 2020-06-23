from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Meta class is where you put extra information
    class Meta:
        # abstact model is a model that does not go into the database by itself
        abstract = True