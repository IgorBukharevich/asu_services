from django.urls import path

from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name='task_list' ),
    path('task_detail/<slug:slug>', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<slug:slug>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<slug:slug>/delete', TaskDeleteView.as_view(), name='task_delete'),
]
