from django.contrib import admin
from django.contrib.admin import site,ModelAdmin

from .models import Song
from .models import Podcast
from .models import AudioBook

# Register your models here.
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(AudioBook)
