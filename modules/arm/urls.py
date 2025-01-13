from django.urls import path
from .views import ArmListView, ArmDetailView


urlpatterns = [
    path('arm_list/', ArmListView.as_view(), name='arm_list'),
    path('arm_detail/<str:slug>', ArmDetailView.as_view(), name='arm_detail'),
]
