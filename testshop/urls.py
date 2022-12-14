from django.urls import path
from django.urls import re_path as url
from .views import ProductsListView,ProductDetailView
urlpatterns = [
    path('api/products',ProductsListView.as_view()),
    url(r'^api/products/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product_detail'),
    ]
