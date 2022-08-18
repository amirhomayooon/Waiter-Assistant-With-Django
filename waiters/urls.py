from django.contrib import admin
from django.urls import path
from menu.views import menu, request_waiter, waiter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu),
    path('request', request_waiter),
    path('waiter', waiter)
]
