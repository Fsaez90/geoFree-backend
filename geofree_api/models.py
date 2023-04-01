from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.utils import timezone
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
    timedate_creation = models.DateTimeField(auto_now=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    # increase max length
    condition = models.CharField(max_length= 200, null=True)
    categories = models.TextField(max_length=200, null=True)
    category_ml = models.CharField(max_length=200, null=True)
    point = models.PointField(null=True)
    views = models.IntegerField(default=0, null=True)
    likes = models.IntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.point = Point(self.longitude, self.latitude)
        if self.categories:
            self.category_ml = self.categories.split(',')[0].strip()
        super().save(*args, **kwargs) 

    @property
    def item_age(self):
        time_diff = timezone.now() - self.timedate_creation
        # Get total seconds
        total_seconds = int(time_diff.total_seconds())
        # Calculate days, hours, and minutes
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        # Return formatted string
        return f"{days} days, {hours} hours, {minutes} minutes"

class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_path, default="", null=True, blank=True)

