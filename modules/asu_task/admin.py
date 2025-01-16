from django.contrib import admin

from .models import Task

@admin.register(Task)
class DepartmentAdmin(admin.ModelAdmin):
    """Админ-панель подразделения"""
    list_display = (
        'id', 'task_num', 'slug', 'publish_status', 'time_create',
        'time_update', 'author'
    )
    list_display_links = ('task_num', 'slug')
    prepopulated_fields = {'slug': ('task_num', )}

    fieldsets = (
        ('Основная информация', {'fields': ('task_num', 'author', 'department', 'slug', 'publish_status', 'fixed')}),
        ('Описание', {'fields': ('description',)})
    )
