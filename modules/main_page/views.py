from django.shortcuts import render
from django.views.generic import ListView

from .models import TaskMPAsu, TitleMainPage


def view_title(request):
    """give_s is models TitleMainPage pk=1(title)
       give_S is models TaskMPAsu all objects
    """
    # TODO: задачи можно будет вытянуть из другого АПП на главную страницу. Так же там могут находится и О НАС КОНТАКТЫ
    title = TitleMainPage.objects.get(pk=1)
    tasks = TaskMPAsu.objects.all()
    return render(
        request,
        template_name='main_page/main_page.html',
        context={'title_asu': title, 'tasks_asu': tasks}
    )
