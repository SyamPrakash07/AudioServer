from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("", views.choice, name="choice"),
    path("Podcast", views.podcast, name="podcast"),
    path("Audiobook", views.audiobook, name="audiobook"),

]