from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Product
from django.utils import timezone

def validate_price(self):
    if self['Price'] < 0 :
        raise ValidationError("Price should be bigger or equal to zero")
    return self['Price']

class ProductSerializer(serializers.ModelSerializer):
    Price = serializers.DecimalField(max_digits=8, decimal_places=2 , validators=[validate_price])
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        image_url = representation.get('image', None)

        if image_url:
            representation['image'] = image_url.replace('localhost', 'teqneia.com')

        return representation
    
    
    def create(self, validated_data):
        validated_data['Name'] = validated_data['Name'].lower()
        return super().create(validated_data)
    
    class Meta:
        model = Product
        fields = ['id', 'Price']