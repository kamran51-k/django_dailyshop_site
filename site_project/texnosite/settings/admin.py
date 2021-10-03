from django.contrib import admin

from settings.models import CategoryModel, StyleModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(StyleModel)