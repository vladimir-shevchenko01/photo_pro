from django.contrib import admin

from src.apps.homepage.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title_big",
        "title_small",
        "button_name",
        "is_published",
        "image",
    )

    list_editable = (
        "is_published",
        "title_big",
        "title_small",
    )
