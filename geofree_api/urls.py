from django.urls import path
from . import views
# def upload_path(instance, filename):
#     return '/'.join(['item', str(instance.id), filename])
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('item-list/', views.itemList, name="item-list"),
    path('item-detail/<str:pk>', views.itemDetail, name="item-detail"),
    path('item-create/', views.itemCreate, name="item-create"),
    path('item-update/<str:pk>', views.itemUpdate, name="item-update"),
    path('item-delete/<str:pk>', views.itemDelete, name="item-delete"),
    path('item-list-distance/', views.itemListDistance, name="item-list-distance"),
]