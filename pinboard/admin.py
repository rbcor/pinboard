from django.contrib import admin

from pinboard.models import Pin,Tag

admin.site.register(Pin)

admin.site.register(Tag)
