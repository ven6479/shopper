from django.test import TestCase
from testshop.models import Product,Category
from testshop.serializers import ProductDetailSerialiser

class ProductSerializerTestCase(TestCase):
    """
    Тестируем Изменчивость Полей/Вывода сериализатора
    """
    def test_get(self):
        category1 = Category.objects.create(title='Кроссовки')
        category2 = Category.objects.create(title='Ботинки')
        product1 = Product.objects.create(title='Adidas', sku='1120',price = '1000.00',category=category1, status='in stock')
        product2 = Product.objects.create(title='Versace', sku='2230', price = '2000.00',category=category2, status='in stock')
        data = ProductDetailSerialiser([product1, product2], many=True).data
        expected_data = [
            {
                'id':product1.id,
                'title':'Adidas',
                'sku':'1120',
                'slug':'adidas-1120',
                'status':'in stock',
                'price':'1000.00',
                'image':None,
                'category': category1.id,
            },
            {
                'id': product2.id,
                'title': 'Versace',
                'sku': '2230',
                'slug': 'versace-2230',
                'status': 'in stock',
                'price' : '2000.00',
                'image': None,
                'category': category2.id,
            }
        ]
        self.assertEqual(data,expected_data)