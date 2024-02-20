from django.contrib import admin

from src.apps.about.models import AboutMe


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_published",
        "upper_text",
        "down_text",
        "list_first_line",
        "list_second_line",
        "list_third_line",
    )

    list_editable = ("is_published",)
