from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('registro',views.registro, name='registro'),
    
]