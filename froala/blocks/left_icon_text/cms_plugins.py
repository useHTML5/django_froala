# coding: utf-8
from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


@plugin_pool.register_plugin
class FroalaLeftIconText(CMSPluginBase):
    module = "Блоки стандартные"
    model = models.ModelFroalaLeftIconText
    name = 'Иконка слева и текст'
    render_template = 'blocks/left_icon_text/plugin.html'
    allow_children = True
