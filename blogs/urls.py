from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('titles/<int:title_id>/', views.title, name='title'),
]
