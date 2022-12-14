from rest_framework import serializers
from .models import Product

class ProductDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['image'] = {'path':str(representation['image']).split('/',3)[3],'format':['jpg','png','wedp']}
        except:
            representation['image'] = 'Неверный путь для файла/нет файла'
        return representation
