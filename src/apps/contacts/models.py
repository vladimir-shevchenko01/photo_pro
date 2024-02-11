from django.db import models

from src.core.models import PublishedModel


class Contacts(PublishedModel):
    """Contacts model."""

    title = models.CharField(
        "Заголовок",
        max_length=32,
        help_text="максимальная длинна поля 32 символа",
    )
    title_text = models.TextField(
        "Описание под заголовком",
        max_length=512,
        help_text="максимальная длина поля 512 символов",
    )
    address = models.CharField(
        "Адрес",
        max_length=120,
        help_text="максимальная длинна поля 120 символов",
    )
    phone_number = models.CharField(
        "Номер телефона",
        max_length=120,
        help_text="максимальная длинна поля 120 символа",
    )
    email = models.EmailField(
        "email",
        max_length=120,
        help_text="максимальная длинна поля 120 символа",
    )

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title
