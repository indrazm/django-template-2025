from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.consumers import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
]

websocket_urlpatterns = [
    re_path(
        r"ws/notification/(?P<notification_id>\w+)/$", NotificationConsumer.as_asgi()
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
