from django.urls import path
from .views import ArmListView


urlpatterns = [
    path('arm_list/', ArmListView.as_view(), name='arm_list'),
]
