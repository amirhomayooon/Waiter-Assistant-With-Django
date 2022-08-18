import os
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from menu.consumers import WaitingConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waiters.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('waiting', WaitingConsumer.as_asgi())
        ])
    )
})
