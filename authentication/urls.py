from django.urls import path

from .views import ObtainAuthToken,UserCreate

urlpatterns = [
    path('login', ObtainAuthToken.as_view(), name='token_create'),
    path('signup', UserCreate.as_view(), name='userCreate'),
    # path('config', Config.as_view(), name='Config'),

]