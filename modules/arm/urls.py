from django.urls import path
from .views import ArmListView, ArmDetailView, ArmCreateView, ArmUpdateView, ArmDeleteView

urlpatterns = [
    path('arm_list/', ArmListView.as_view(), name='arm_list'),
    path('arm_detail/<slug:slug>', ArmDetailView.as_view(), name='arm_detail'),
    path('arm/create/', ArmCreateView.as_view(), name='arm_create'),
    path('arm/<slug:slug>/update/', ArmUpdateView.as_view(), name='arm_update'),
    path('arm/<slug:slug>/delete', ArmDeleteView.as_view(), name='arm_delete'),
]
