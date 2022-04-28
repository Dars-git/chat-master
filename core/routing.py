from core import consumers

from django.urls import include, re_path

websocket_urlpatterns = [
    re_path(r'^ws$', consumers.ChatConsumer),
]
