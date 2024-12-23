from django.db import models
from django.contrib.auth import get_user_model
from mptt.fields import TreeForeignKey

from modules.services.utils import unique_slugify

User = get_user_model()


class Department(models.Model):
    """Модель Подразделений"""
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительское подразделение',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
    )
    publish_status = models.CharField(
        verbose_name='Статус публикации',
        choices=STATUS_OPTIONS,
        default='published',
        max_length=10,
    )
    time_create = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Дата обновления',
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='authro_dep_add',
    )
    updater = models.ForeignKey(
        to=User,
        verbose_name='Обновил',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updater_dep',
    )
    fixed = models.BooleanField(
        verbose_name='Зафиксировано',
        default=False,
    )

    class MPTTMeta:
        """Сортировка по вложенности"""
        order_insertion_by = ('title',)

    class Meta:
        """Сортировка, название модели в админ панели, таблица с данными"""
        db_table = 'app_dep'
        verbose_name = 'Подразделение/Отдел/Отделение'
        verbose_name_plural = 'Подразделения/Отделы/Отделения'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Сохранение полей модели при их отсутствии"""
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)


class Arm(models.Model):
    """Модель АРМ"""
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    num_arm = models.PositiveIntegerField(
        verbose_name='АРМ',
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=255,
    )
    ip_addr = models.TextField(
        verbose_name='IP-адрес/а',
        max_length=300,
    )
    department = models.ForeignKey(
        to=Department,
        verbose_name='Подразделение/Отделение/Отдел',
        on_delete=models.PROTECT,
        related_name='arm_dep',
    )
    publish_status = models.CharField(
        verbose_name='Статус публикации',
        choices=STATUS_OPTIONS,
        default='published',
        max_length=10,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    time_create = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Дата обновления',
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='authro_arm_add',
    )
    updater = models.ForeignKey(
        to=User,
        verbose_name='Обновил',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updater_arm',
    )
    fixed = models.BooleanField(
        verbose_name='Зафиксировано',
        default=False,
    )

    # object = ArmManager() - возможно добавление кастомного менеджера

    class Meta:
        db_table = 'app_arm'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create', 'publish_status'])]
        verbose_name = 'АРМ'
        verbose_name_plural = 'АРМы'

    def __str__(self):
        return self.num_arm

    def save(self, *args, **kwargs):
        """Сохранение полей модели при их отсутствии"""
        if not self.slug:
            self.slug = unique_slugify(self, self.num_arm)
        super().save(*args, **kwargs)
