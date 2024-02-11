from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from src.apps.gallery.models import Category, DetailPageImages, MainBanner
from config.settings import IMAGE_UP_QTY, IMAGE_DOWN_QTY


class GalleryListView(ListView):
    """Список категорий фотосъемок."""

    model = Category
    template_name = "gallery/gallery_list_of_categories.html"

    def get_context_data(self, **kwargs):
        """
        Контекст: категории фото, длинна списка объектов категории
        """
        context = super().get_context_data(**kwargs)
        foto_cat = (
            Category.objects.all().filter(is_published=True).order_by("title")
        )
        context["foto_cat"] = foto_cat
        context["list_of_index"] = list(range(len(foto_cat)))
        # Получаем объект баннера последнего добавленного
        main_banner = MainBanner.objects.order_by("title").last()
        context["main_banner"] = main_banner
        return context


class GalleryDetailView(DetailView):
    model = Category
    template_name = "gallery/gallery_category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_banner = MainBanner.objects.order_by("-id").last()
        context["main_banner"] = main_banner
        category_slug = self.object.slug
        cat_desc = get_object_or_404(
            Category, slug=category_slug, is_published=True
        )
        context["cat_desc"] = cat_desc
        image_up = (
            DetailPageImages.objects.select_related(
                "category",
            )
            .filter(
                is_published=True,
                category__is_published=True,
                category__slug=category_slug,
            )
            .order_by("title")[:IMAGE_UP_QTY]
        )
        image_down = (
            DetailPageImages.objects.select_related(
                "category",
            )
            .filter(
                is_published=True,
                category__is_published=True,
                category__slug=category_slug,
            )
            .order_by("title")[IMAGE_UP_QTY:IMAGE_DOWN_QTY]
        )
        context["image_down"] = image_down
        context["image_up"] = image_up
        return context
