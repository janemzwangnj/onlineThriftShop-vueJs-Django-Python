from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('shopcards/', views.ShopcardList.as_view(), name='shopcard_list'),
    path('shopcards/<int:pk>', views.ShopcardDetail.as_view(), name='shopcard_detail')
]
