from django.contrib import admin
from .models import Tag, MovieTag

# Register your models here.

admin.site.register(Tag)
admin.site.register(MovieTag)
