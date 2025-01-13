from django.shortcuts import render


def faq_view(request):
    return render(request, template_name='faq/faq_page.html')
