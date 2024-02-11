from django.urls import path

from src.apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.MyContactsView.as_view(), name="contacts"),
]
