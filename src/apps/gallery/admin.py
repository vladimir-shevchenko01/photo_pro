from django.contrib import admin

from src.apps.gallery.models import Category, DetailPageImages, MainBanner


@admin.register(MainBanner)
class MainBannerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "title_text",
        "image",
    )

    list_editable = (
        "title_text",
        "image",
    )

    list_display_links = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
    )

    list_editable = (
        "title",
        "is_published",
    )


@admin.register(DetailPageImages)
class DetailPageImagesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_published",
        "category",
        "image",
    )

    list_editable = ("is_published",)
