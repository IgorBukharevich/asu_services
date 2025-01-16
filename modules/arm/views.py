from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArmCreateForm, ArmUpdateForm
from .models import Arm


class ArmListView(ListView):
    model = Arm
    template_name = 'arm_asu/arm_list.html'
    context_object_name = 'arm_list'
    queryset = Arm.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список АРМов'
        return context


class ArmDetailView(DetailView):
    model = Arm
    template_name = 'arm/arm_detail.html'
    context_object_name = 'arm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.num_arm
        return context


class ArmCreateView(CreateView):
    """Представление: создание материалов на сайте"""
    model = Arm
    success_url = reverse_lazy('arm_list')
    template_name = 'arm/arm_create.html'
    form_class = ArmCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление АРМ на сайт'
        return context

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class ArmUpdateView(UpdateView):
    """Представление: обновление материалов на сайте"""
    model = Arm
    success_url = reverse_lazy('arm_list')
    template_name = 'arm/arm_update.html'
    form_class = ArmUpdateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление АРМ: {self.object.num_arm}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArmDeleteView(DeleteView):
    """Представление: удаление АРМ"""
    model = Arm
    success_url = reverse_lazy('arm_list')
    template_name = 'arm/arm_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление статьи: {self.object.num_arm}'
        return context
