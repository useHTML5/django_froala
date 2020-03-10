# coding: utf-8
from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


# from django.utils.translation import ugettext as _
# from django.contrib import admin
# from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline

#
# @plugin_pool.register_plugin
# class HomeServicesPlugin(CMSPluginBase):
#     model = HomeServicesPluginModel
#     name = 'Главная - Услуги'
#     render_template = 'siling/plugin.html'
#     allow_children = True
# cache = False

# class InlinePic(admin.TabularInline):
#     model = HomeGalleryPicPluginModel
#     extra = 0

# inlines = [InlinePic, ]

@plugin_pool.register_plugin
class FroalaLeftBigImg3pluses(CMSPluginBase):
    module = "Преимущества блоки"
    model = models.ModelLeftBigImg3pluses
    name = 'Большое изображение слева и 3 плюса справа'
    render_template = 'froala_features/leftbigimg_3pluses/plugin.html'
