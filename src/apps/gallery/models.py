from django.db import models
from pytils.translit import slugify

from src.core.models import PublishedModel


class MainBanner(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=32,
        help_text="максимальная длинна поля 32 символа",
    )
    title_text = models.TextField(
        "Описание под заголовком",
        max_length=120,
        help_text="максимальная длина поля 120 символов",
    )
    image = models.ImageField(
        "Изображение",
        upload_to="images/gallery_main/",
        help_text="Размер изображения 1920х900px",
    )

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title_text


class Category(PublishedModel):
    title = models.CharField(
        "Категория",
        max_length=24,
        help_text="максимальная длинна поля 24 символа",
    )
    foto_title = models.CharField(
        "Тип съемки",
        max_length=32,
        help_text="максимальная длинна поля 32 символа",
    )
    title_text = models.TextField("Описание съемки")
    image = models.ImageField(
        "Заглавное изображение",
        upload_to="images/foto_type/",
        help_text="Размер изображения 915х700px",
    )
    slug = models.SlugField(
        "Адрес для страницы с заметкой",
        max_length=100,
        unique=True,
        blank=True,
        help_text=(
            "Укажите адрес для страницы заметки. Используйте только "
            "латиницу, цифры, дефисы и знаки подчёркивания"
        ),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            max_slug_length = self._meta.get_field("slug").max_length
            self.slug = slugify(self.title)[:max_slug_length]
        super().save(*args, **kwargs)


class DetailPageImages(PublishedModel):
    title = models.CharField(
        "Инфо", max_length=24, help_text="максимальная длинна поля 24 символа"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="фото",
    )
    image = models.ImageField(
        "Изображение",
        upload_to="images/gallery_detail_up/",
        help_text="Верхний ряд. Размер изображения 580x400px",
    )

    class Meta:
        verbose_name = "фото для категории"
        verbose_name_plural = "Фото категорий"

    def __str__(self):
        return self.title
