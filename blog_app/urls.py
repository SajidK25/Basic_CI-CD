from django.urls import path
from . import views

urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('<int:pk>/', views.blog, name='blog'),
]