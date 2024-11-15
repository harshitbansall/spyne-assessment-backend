from rest_framework import serializers

from .models import *


class UserAllProductsSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    images = serializers.SerializerMethodField("get_image_urls")

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'title',
                  'description', 'price', 'tags', 'images')

    def get_image_urls(self, obj):
        return [image.image.url for image in obj.images.all()]
