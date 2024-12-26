from django.contrib import admin

from .models import TaskMPAsu, TitleMainPage


@admin.register(TaskMPAsu)
class TaskMPAsuAdmin(admin.ModelAdmin):
    """Админ-панель модели Задачи Главной страницы АСУ"""
    list_display = ('id', 'title', 'slug', 'time_create', 'time_update', 'publish_status')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'publish_status')}),
        ('Описание', {'fields': ('short_description', )})
    )


@admin.register(TitleMainPage)
class TitleMainPageAdmin(admin.ModelAdmin):
    """Админ-панель модели Заголовки Главной страницы"""
    list_display = ('id', 'title', 'slug', 'time_create', 'time_update', 'publish_status', 'fixed')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'publish_status', 'fixed')}),
        ('Описание', {'fields': ('short_description', )})
    )
