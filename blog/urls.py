from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.blog, name='Home'),
    path('exemplo/', views.exemplo, name= 'Exemplo'),

]
