from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'website'

urlpatterns = [

    path('tasks/',views.TaskListView.as_view(),name='task-list'),
    path('tasks/<int:pk>/',views.TaskDetailView.as_view(),name='task-detail'),
   path('tasks/create/',views.TaskCreateView.as_view(),name='task-create'),
    # path('task/<int:pk>/edit/',views.TaskEditView.as_view(),name='task-edit'),
    path('tasks/<int:pk>/delete/',views.TaskDeleteView.as_view(),name='task-delete'),


]