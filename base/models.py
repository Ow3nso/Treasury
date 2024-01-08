from django.db import models

# Create your models here.
class Process_Statement(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    giving = models.CharField(max_length=1000, blank=False)
    amount = models.FloatField(blank=False)

    def __str__(self):
        return self.name 