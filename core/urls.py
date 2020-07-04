from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogdetail, name='blogdetail'),
]