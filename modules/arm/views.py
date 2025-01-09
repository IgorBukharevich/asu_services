from django.shortcuts import render
from django.views.generic import ListView

from .models import Arm, Department


class ArmListView(ListView):
    model = Arm
    template_name = 'arm_asu/arm_list.html'
    context_object_name = 'arm_list'
    queryset = Arm.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список АРМов'
        return context
