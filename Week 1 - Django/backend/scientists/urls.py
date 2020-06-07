from django.urls import path

from .views import ScientistView

urlpatterns = [path("scientists/", ScientistView.as_view())]
