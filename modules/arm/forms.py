from django import forms

from .models import Arm


class ArmCreateForm(forms.ModelForm):
    """Форма добавления АРМ на сайт"""
    class Meta:
        model = Arm
        fields = (
            'num_arm', 'ip_addr', 'department', 'description', 'status'
        )

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под Bootstrap"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class ArmUpdateForm(ArmCreateForm):
    """Форма обновления АРМ на сайте"""
    class Meta:
        model = Arm
        fields = ArmCreateForm.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под Bootstrap"""
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })
