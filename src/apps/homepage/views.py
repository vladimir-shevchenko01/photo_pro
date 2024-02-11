from django.shortcuts import render

from src.apps.homepage.models import Slider


def index(request):
    """Homepage view"""

    template = "homepage/index.html"
    sliders = Slider.sliders.all()
    context = {"sliders": sliders}
    return render(request, template, context)
