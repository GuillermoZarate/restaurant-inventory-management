from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout_request, name='logout'),
    path('inventory/', views.inventory, name="inventory"),
    path('menu/', views.inventory, name="menu"),
    path('purchases/', views.inventory, name="purchases"),
]