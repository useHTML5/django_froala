# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField


# from adminsortable.models import SortableMixin


class SilingPluginModel(CMSPlugin):
    green = models.CharField(verbose_name="Зеленая пелена", max_length=255, blank=True, null=True,
                             choices=(('left', 'left'), ('right', 'right')))
    text_side = models.CharField(verbose_name="Сторона для текста", max_length=255, default="left",
                                 choices=(('left', 'left'), ('right', 'right')))
    pic = FilerImageField(verbose_name='Изображение', related_name='pic_siling', blank=True, null=True,
                          on_delete=models.SET_NULL)
