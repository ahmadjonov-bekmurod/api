from django.urls import path
from .views import ToDoListCreateAPIView, ToDoRetrieveUpdateDestroyAPIView, AudioFileView, AudioFileListView, AudioFileUploadView

urlpatterns = [
    path('todos/', ToDoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),
    path('audio/', AudioFileListView.as_view(), name='audio-file-list'),
    path('audio/<str:filename>/', AudioFileView.as_view(), name='audio-file'),
    path('audio/upload/', AudioFileUploadView.as_view(), name='audio-file-upload'),
]
