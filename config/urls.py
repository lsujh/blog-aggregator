from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog.views import robots_txt
from blog.sitemaps import CategoriesSitemap, PostsSitemap


sitemaps = {
    "categories": CategoriesSitemap,
    "posts": PostsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('post/', include('blog.urls', namespace='blog')),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path('contact/', include('contact.urls', namespace='contact')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
    path("robots.txt", robots_txt),
    path('', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
