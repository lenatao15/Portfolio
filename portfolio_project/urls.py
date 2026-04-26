from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # On Render, we can use this to serve media files if we're not using a persistent disk
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

