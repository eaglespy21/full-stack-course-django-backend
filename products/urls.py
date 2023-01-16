from django.contrib import admin
from django.urls import include, path
from .views import ProductCategoryListView, MakerListView, ProductListView

app_name = "products"  # Has to be the name of your app - folder name

urlpatterns = [
    path('', ProductListView.as_view(), name='products-list-view'),
    path('categories', ProductCategoryListView.as_view(), name='categories-list'),
    path('makers', MakerListView.as_view(), name='makers-list')
]
