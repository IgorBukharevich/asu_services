from enum import unique

from django.db import models

from django.contrib.auth import get_user_model

from modules.services.utils import unique_slugify

User = get_user_model()


class TitleMainPage(models.Model):
    """Модель ЗаголовокГловной страницы"""
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='SLUG',
        max_length=255,
        unique=True,
        blank=True,
    )
    publish_status = models.CharField(
        verbose_name='Статус публикации',
        choices=STATUS_OPTIONS,
        default='published',
        max_length=10,
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        max_length=300,
    )
    time_create = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    fixed = models.BooleanField(
        verbose_name='Зафиксировано',
        default=False,
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='title_author_add',
    )
    updater = models.ForeignKey(
        to=User,
        verbose_name='Обновил',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updater_main_page',
    )

    class Meta:
        db_table = 'app_title_main_page'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['fixed', 'time_create', 'publish_status'])]
        verbose_name = 'Шапка главной страницы'
        verbose_name_plural = 'Шапки главной страницы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Сохранение полей модели при их отсутствии"""
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)


class TaskMPAsu(models.Model):
    """Модель ЗадачиГлавнойСтраницыАсу"""

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    title = models.CharField(
        verbose_name='Загловок',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='SLUG',
        max_length=255,
    )
    publish_status = models.CharField(
        verbose_name='Статус публикации',
        choices=STATUS_OPTIONS,
        default='published',
        max_length=10,
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        max_length=300,
    )
    time_create = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    fixed = models.BooleanField(
        verbose_name='Зафиксировано',
        default=False,
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='task_mp_author_add',
    )
    updater = models.ForeignKey(
        to=User,
        verbose_name='Обновил',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updater_task_main_page',
    )

    class Meta:
        db_table = 'app_task_mp_asu'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['fixed', 'time_create', 'publish_status'])]
        verbose_name = 'Задача главной страницы'
        verbose_name_plural = 'Задачи главной страницы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Сохранение полей модели при их отсутствии"""
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)
