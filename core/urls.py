from django.urls import path
from . import views


# application namespace, allows urls to be organized by apps
app_name = 'core'

urlpatterns = [
    # portfolio homepage pattern
    path('', views.home, name='home'),

    # post patterns
    path('post/', views.post_list, name='post_list'),
    # path('post/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('post/tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
]