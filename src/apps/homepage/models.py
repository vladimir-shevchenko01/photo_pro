from django.db import models
from django.db.models import CharField

from src.core.models import PublishedModel


class SliderManager(models.Manager):
    """
    Define a custom manager for the Post model.
    """

    def get_queryset(self):
        # Override the default get_queryset method
        # to apply additional filters to the QuerySet[Post].
        return (
            super()
            .get_queryset()
            .filter(
                is_published=True,
            )
        )


class Slider(PublishedModel):
    title_big = models.CharField(
        max_length=32,
        verbose_name="Заголовок",
    )
    title_small = models.CharField(
        max_length=32,
        verbose_name="Заголовок 2",
    )
    button_name = models.CharField(
        max_length=24,
        verbose_name="Кнопка в галерею",
    )
    image = models.ImageField(
        "Изображение",
        upload_to="images/slider/",
        help_text="Размер изображения 1920х900px",
    )

    objects = models.Manager()
    sliders = SliderManager()

    class Meta:
        verbose_name = "слайдер"
        verbose_name_plural = "Слайдеры"

    def __str__(self) -> CharField:
        return self.title_big
