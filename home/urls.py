from django.urls import path

from .views import UserProductsView

urlpatterns = [
    path('products', UserProductsView.as_view(), name='products_view'),
    # path('signup', UserCreate.as_view(), name='userCreate'),
]
