from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from modules.arm.models import Department
from modules.services.utils import unique_slugify

User = get_user_model()


class Task(models.Model):
    """Модель Заявки"""
    # class TaskManager(models.Manager):
    #     """Кастомный менеджер для модели Заявок"""
    #     def all(self):
    #         """Список заявок (SQL запрос с фильтрацией для страницы заявок"""
    #         return
    STATUS_TASK = (
        ('active', 'Актина'),
        ('in progress', 'В процессе'),
        ('completed', 'Выполнена')
    )
    STATUS_PUBLISH = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )
    task_num = models.CharField(
        verbose_name='Номер заявки',
        max_length=255,
        unique=True,
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=255,
        blank=True,
        unique=True,
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='author_task_add',
    )
    department = models.ForeignKey(
        to=Department,
        verbose_name='Подразделение/Отдел/Отделение',
        on_delete=models.PROTECT,
        related_name='author_dep',
    )
    description = models.TextField(
        verbose_name='Описание проблемы',
    )
    time_create = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True,
    )
    status_task = models.CharField(
        verbose_name='Статус заявки',
        choices=STATUS_TASK,
        default='active',
    )
    publish_status = models.CharField(
        verbose_name='Статус публикации',
        choices=STATUS_PUBLISH,
        default='published',
    )
    fixed = models.BooleanField(
        verbose_name='Зафиксировано',
        default=False,
    )

    class Meta:
        db_table = 'app_task_asu'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create', 'publish_status'])]
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.task_num}'

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.task_num)
        super().save(*args, **kwargs)
