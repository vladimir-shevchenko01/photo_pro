from django.urls import path

from src.apps.about import views

app_name = "about"

urlpatterns = [
    path("", views.AboutMeView.as_view(), name="about_me"),
]
