
from rest_framework import serializers
from .models import *
from seller.serializers import SellerSerializer
from category.serializers import CategorySerializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = [
                    'uuid',
                    'code',
                    'title_fa', 
                    'title_en', 
                    'slug', 
                    'total_inventory', 
                    'category', 
                    'active_collection',
                    'is_promotion',
                    'is_active',
                    'description',
                    'main_image',
        ]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = [
                    'uuid',
                    'title_fa', 
                    'title_en', 
        ]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
                    'uuid',
                    'title_fa',
                    'title_en',
                    'hex_code', 
        ]
 
class VarietySerializer(serializers.ModelSerializer):
    seller = SellerSerializer()
    color = ColorSerializer(many=True , read_only=True)
    size = SizeSerializer(many=True , read_only=True)

    class Meta:
        model = Variety
        fields = [
                    'uuid',
                    'color',
                    'size',
                    'rrp_price', 
                    'is_active', 
                    'selling_price', 
                    'inventory', 
                    'max_quantity', 
                    'seller', 
        ]
        

class VarietyImageSerializer(serializers.HyperlinkedModelSerializer):
    variety = VarietySerializer()
    class Meta:
        model = VarietyImage
        fields = [
                    'title_fa',
                    'title_en',
                    'url', 
                    'variety', 
        ]
         


























