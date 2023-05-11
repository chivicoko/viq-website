from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/update', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete', TaskDelete.as_view(), name='post-delete'),
]