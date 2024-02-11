from django.contrib import admin

from src.apps.contacts.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        "is_published",
        "title",
        "title_text",
        "address",
        "phone_number",
        "email",
    )

    list_editable = (
        "address",
        "phone_number",
        "email",
    )

    list_display_links = ("is_published",)
