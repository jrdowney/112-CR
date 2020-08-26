from django.urls import path 
from . import views

# valid routes for rental app
urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('catalog', views.catalog_ssr, name="catalog1"),
    path('catalog2', views.catalog_csr, name="catalog2"),
    path('details/<int:id>', views.details, name="details"),
    path('contact', views.contact, name="contact"),
]