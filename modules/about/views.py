from django.shortcuts import render

def about_view(request):
    """Представление: отображение страницы ABOUT -О нас"""
    return render(request, template_name='about/about_page.html')
