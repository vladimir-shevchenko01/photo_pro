from django.views.generic import TemplateView

from src.apps.contacts.models import Contacts
from src.apps.gallery.models import MainBanner


class MyContactsView(TemplateView):
    model = Contacts
    template_name = "contacts/contact.html"

    def get_context_data(self, **kwargs):
        """Generate the data to be displayed on the page."""
        context = super().get_context_data(**kwargs)
        main_banner = MainBanner.objects.order_by("-id").last()
        context["main_banner"] = main_banner
        contacts = Contacts.objects.order_by("-id").last()
        context["contacts"] = contacts
        return context
