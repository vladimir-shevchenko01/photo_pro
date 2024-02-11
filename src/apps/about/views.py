from django.views.generic import TemplateView
from src.apps.about.models import AboutMe


class AboutMeView(TemplateView):
    """About me page."""

    model = AboutMe
    template_name = "about/aboutme.html"
    context_object_name = "about_note"

    def get_context_data(self, **kwargs):
        """Generate the data to be displayed on the page."""
        context = super().get_context_data(**kwargs)
        about_note = AboutMe.objects.order_by("-id").last()
        context["about_note"] = about_note
        return context
