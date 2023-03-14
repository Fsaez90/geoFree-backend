from django.db import models

# Create your models here.

def upload_path(instance, filename):
    return '/'.join(['item', str(instance.item), filename])


class Item(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length= 200, null=True)
    available = models.BooleanField(default=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    # increase max length
    condition = models.CharField(max_length= 20, null=True)

class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_path, default="", null=True, blank=True)