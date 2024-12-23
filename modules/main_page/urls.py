from django.urls import path

from .views import view_title


urlpatterns = [
    path('', view_title, name='home'),
]
