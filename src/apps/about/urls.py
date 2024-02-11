from django.urls import path

from src.apps.about import views

app_name = "about"

urlpatterns = [
    # path('', views.about, name='about_me'),
    path("", views.AboutMeView.as_view(), name="about_me"),
]
