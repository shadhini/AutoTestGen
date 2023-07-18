from django.urls import path

from . import views

urlpatterns = [
    path("", views.testbot_view, name="testbot_view"),
]
