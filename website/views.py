from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 2
    ordering = "-id"


class TaskDetailView(DetailView):

    model = Task


# class IndexView(TemplateView):
#     template_name = 'task_list.html'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "is_done", "created_date"]
    success_url = "/website/tasks/"

    def form_invalid(self, form):
        print("FORM ERRORS:", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = "/website/tasks/"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/website/tasks/"
