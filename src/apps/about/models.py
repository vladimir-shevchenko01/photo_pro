from django.db import models

from src.core.models import PublishedModel


class AboutMe(PublishedModel):
    title = models.CharField(
        "Заголовок",
        max_length=32,
        help_text="Максимальная длинна поля 32 символа",
    )
    upper_text = models.TextField(
        "Текст верхний обзац",
        max_length=600,
        help_text="Максимальная длина поля 600 символов",
    )
    down_text = models.TextField(
        "Текст нижний обзац",
        max_length=600,
        help_text="Максимальная длина поля 600 символов",
    )
    list_first_line = models.CharField(
        "Первая строка списка",
        max_length=80,
        help_text="Максимальная длинна поля 80 символа",
    )
    list_second_line = models.CharField(
        "Вторая строка списка",
        max_length=80,
        help_text="Максимальная длинна поля 80 символа",
    )
    list_third_line = models.CharField(
        "Третья строка списка",
        max_length=80,
        help_text="Максимальная длинна поля 80 символа",
    )
    image = models.ImageField(
        "Изображение",
        upload_to="images/gallery_about/",
        help_text="Размер изображения 1920х900px",
    )

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def __str__(self):
        return self.title
