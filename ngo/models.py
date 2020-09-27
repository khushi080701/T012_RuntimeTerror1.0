from django.db import models

# Create your models here.
class Crop(models.Model):
    cropName = models.CharField(max_length=100)
    cropQuantity = models.IntegerField()
    

    def __str__(self):
        return self.cropName
