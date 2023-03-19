from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('item-list/', views.itemList, name="item-list"),
    path('item-detail/<str:pk>', views.itemDetail, name="item-detail"),
    path('item-create/', views.itemCreate, name="item-create"),
    path('item-update/<str:pk>', views.itemUpdate, name="item-update"),
    path('item-delete/<str:pk>', views.itemDelete, name="item-delete"),
    path('views-update/<str:pk>', views.viewsUpdate, name="views-update"),
    path('like-item/<str:pk>', views.likesUpdate, name="like-item"),
    path('dislike-item/<str:pk>', views.dislikeUpdate, name="dislike-item"),
    path('item-list-distance/', views.itemListDistance, name="item-list-distance"),
]