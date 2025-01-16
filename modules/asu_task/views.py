from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Task
from .forms import TaskUpdateForm, TaskCreateForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_asu/task_list.html'
    context_object_name = 'task_list'
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список Заявок'
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_asu/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.task_num
        return context


class TaskCreateView(CreateView):
    """Представление: создание материалов на сайте"""
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_asu/task_create.html'
    form_class = TaskCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление Заявки на сайт'
        return context

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    """Представление: обновление материалов на сайте"""
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_asu/task_update.html'
    form_class = TaskUpdateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление Заявки: {self.object.task_num}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    """Представление: удаление Заявки"""
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_asu/task_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление статьи: {self.object.task_num}'
        return context
