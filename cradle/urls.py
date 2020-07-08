from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap


from core.sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls',  namespace='core')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
