from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    #path('category/<int:category_id>/',  views.category, name="category"), # category_id es un parametro dinamico y siempre es una cadena de caracteres
    path('category/<int:category_id>/', views.category, name="category")
]