from django import forms

from .models import Task


class TaskCreateForm(forms.ModelForm):
    """Форма добавления АРМ на сайт"""
    class Meta:
        model = Task
        fields = (
            'task_num', 'author', 'department', 'description', 'publish_status'
        )

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под Bootstrap"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class TaskUpdateForm(TaskCreateForm):
    """Форма обновления АРМ на сайте"""
    class Meta:
        model = Task
        fields = TaskCreateForm.Meta.fields + ('fixed', 'status_task',)

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под Bootstrap"""
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })
