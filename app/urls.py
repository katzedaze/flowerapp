from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('', views.upload, name='upload'),
    path('result/', views.result, name='result'),
]
