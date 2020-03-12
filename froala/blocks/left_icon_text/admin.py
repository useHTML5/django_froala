from django.contrib import admin
from . import models


@admin.register(models.LeftIconTextConf)
class LeftIconTextConfAdmin(admin.ModelAdmin):
    pass
