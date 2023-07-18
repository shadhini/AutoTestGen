from django.urls import path

from . import views

urlpatterns = [
    path("", views.code_quality_checker_view, name="code_quality_checker_view"),
]
