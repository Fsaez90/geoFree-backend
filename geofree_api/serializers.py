from rest_framework import serializers
from .models import Item, ItemImages


class ItemImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemImages
        fields = ["id", "item", "image"]

class ItemSerializers(serializers.HyperlinkedModelSerializer):
    images = ItemImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 10000000, allow_empty_file = False, use_url = False),
        write_only =True
    )
    available = serializers.BooleanField(default=True)
    class Meta:
        model =  Item
        fields = ['id', 'title', 'description', 'available', 'latitude', 'longitude', 'condition', 'point', 'views', 'likes','images', 'uploaded_images']
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        item = Item.objects.create(**validated_data)
        for image in uploaded_images:
            newitem_image = ItemImages.objects.create(item=item, image=image)
        return item