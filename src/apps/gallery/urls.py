from django.urls import path

from src.apps.gallery import views

app_name = "gallery"

urlpatterns = [
    path("", views.GalleryListView.as_view(), name="category_list"),
    path(
        "<slug:slug>/",
        views.GalleryDetailView.as_view(),
        name="category_detail",
    ),
]
