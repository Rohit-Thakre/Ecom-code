from django.urls import path
from . import views

# for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path(''),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
