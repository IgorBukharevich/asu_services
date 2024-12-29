from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Department, Arm


@admin.register(Arm)
class ArmAdmin(admin.ModelAdmin):
    """Админ-панель модели АРМ"""
    list_display = (
        'id', 'num_arm', 'slug',
        'ip_addr', 'department', 'publish_status',
        'time_create', 'time_update', 'author'
    )
    list_display_links = ('num_arm', 'slug')
    prepopulated_fields = {'slug': ('num_arm',)}

    fieldsets = (
        ('Основная информация', {'fields': (
            'num_arm', 'slug', 'ip_addr',
            'department', 'publish_status'
        )}),
        ('Описание', {'fields': ('description', )})
    )


@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    """Админ-панель подразделения"""
    list_display = (
        'tree_actions', 'indented_title', 'id',
        'title', 'slug', 'publish_status', 'time_create',
        'time_update', 'author'
    )
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'parent', 'publish_status')}),
        ('Описание', {'fields': ('description',)})
    )
