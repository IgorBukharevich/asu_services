from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class TitleMainPage(models.Model):
    """Модель ЗаголовокГловной страницы"""
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
    time_create = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Дата обновления',
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
        related_name='author_add',
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
        indexes = [models.Index(fields=['fixed', 'time_create', 'status'])]
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'

    def __str__(self):
        if __name__ == '__main__':
            return self.title
