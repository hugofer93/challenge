from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home/', views.Home.as_view(), name='home')
]
