from django.contrib import admin
from django.urls import path
from signaling.views import video_call

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', video_call),
]