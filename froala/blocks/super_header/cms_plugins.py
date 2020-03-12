# coding: utf-8
from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


# from . import forms

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
class FroalaSuperHeader(CMSPluginBase):
    module = "Блоки стандартные"
    model = models.ModelFroalaSuperHeader
    name = 'Супер заголовок'
    render_template = 'froala_blocks/super_header/plugin.html'
    # form = forms.FormFroalaServiceImgText
