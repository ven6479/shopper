from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from testshop.models import Product,Category
from testshop.serializers import ProductDetailSerialiser
class ProductApiTestCase(APITestCase):
    """
    Тестируем правильность API, статус сервера
    """
    def test_get(self):
        category1 = Category.objects.create(title = 'Кроссовки')
        category2 = Category.objects.create(title='Ботинки')
        product1 = Product.objects.create(title = 'Адидас', sku = '1120', category = category1, status = 'in stock')
        product2 = Product.objects.create(title='Versace', sku = '2230', category = category2, status='in stock')
        serializer_data = ProductDetailSerialiser([product2,product1],many=True).data
        url = '/api/products'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK,response.status_code)
        self.assertEqual(serializer_data,response.data)

# Create your tests here.    title = models.CharField(_('title'), max_length=255)
#     sku = models.CharField(_('sku'), max_length=255, unique=True)
#     slug = models.SlugField(_('slug'), max_length=255,blank=True)
#     category = models.ForeignKey(verbose_name=_('category'), to='Category', on_delete=models.PROTECT, related_name='products')
#     status = models.CharField(_('status'),choices=Status.choices,max_length=255)
#     image = WEBPField(upload_to=image_folder,default=None)