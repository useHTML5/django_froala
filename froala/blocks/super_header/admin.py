from django.contrib import admin
from . import models


@admin.register(models.SuperHeaderConf)
class SuperHeaderConfAdmin(admin.ModelAdmin):
    pass
