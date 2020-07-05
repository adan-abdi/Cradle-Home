from django.urls import path
from . import views


# application namespace, allows urls to be organized by apps
app_name = 'core'

urlpatterns = [
    # portfolio homepage view
    path('', views.home, name='home'),
    # post views
    # path('post/', views.post_list, name='post_list'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]