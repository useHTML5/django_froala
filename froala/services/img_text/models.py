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

class ModelFroalaServiceImgText(CMSPlugin):
    link = PageField(verbose_name='Страница', blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок', blank=True, null=True, max_length=255)
    link_text = models.CharField(verbose_name='Текст ссылки', blank=True, null=True, max_length=255, default='Подробнее')
    pic = FilerImageField(verbose_name='Изображение слева', related_name='+', blank=True, null=True,
                          on_delete=models.SET_NULL)
    html = HTMLField('Текст', blank=True, null=True)
