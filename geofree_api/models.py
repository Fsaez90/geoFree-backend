from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# from django.db import models



# Create your models here.

def upload_path(instance, filename):
    return '/'.join(['item', str(instance.item), filename])


class Categories(models.Model):
    name = models.CharField(max_length=30, null=True)

class Item(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length= 200, null=True)
    available = models.BooleanField(default=True, null=True)
    creation_date = models.DateField(auto_now=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    # increase max length
    condition = models.CharField(max_length= 20, null=True)
    categories = models.TextField(max_length=200, null=True)
    point = models.PointField(null=True)
    views = models.IntegerField(default=0, null=True)
    likes = models.IntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.point = Point(self.longitude, self.latitude)
        super().save(*args, **kwargs) 
   

class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_path, default="", null=True, blank=True)

