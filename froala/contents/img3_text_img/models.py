# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField


# from adminsortable.models import SortableMixin
# pic = FilerImageField(verbose_name='Изображение', related_name='+', blank=True, null=True,on_delete=models.SET_NULL)
# html = HTMLField('Текст', blank=True, null=True)

class ModelFroala3imgTextImg(CMSPlugin):
    pic1 = FilerImageField(verbose_name='Изображение слева 1', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    pic2 = FilerImageField(verbose_name='Изображение слева 2', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    pic3 = FilerImageField(verbose_name='Изображение слева 3', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    pic4 = FilerImageField(verbose_name='Изображение справа', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    html = HTMLField('Текст', blank=True, null=True)
