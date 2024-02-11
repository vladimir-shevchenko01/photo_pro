from django.db import models


class PublishedModel(models.Model):
    """Abstract model, adds the is_published flag."""

    # Date and time user want post to be published.
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть слайдер",
    )

    class Meta:
        abstract = True
