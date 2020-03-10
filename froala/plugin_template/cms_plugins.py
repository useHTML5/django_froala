# coding: utf-8
from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import SilingPluginModel


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
class SilingPlugin(CMSPluginBase):
    module = "Сайт"
    model = SilingPluginModel
    name = 'Тип потолка'
    render_template = 'siling/plugin.html'
    allow_children = True
