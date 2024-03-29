from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.apps.homepage.urls")),
    path("gallery/", include("src.apps.gallery.urls")),
    path("about/", include("src.apps.about.urls")),
    path("contacts/", include("src.apps.contacts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
