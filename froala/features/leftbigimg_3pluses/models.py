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

class ModelLeftBigImg3pluses(CMSPlugin):
    pic_big = FilerImageField(verbose_name='Изображение слева большое', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    pic1 = FilerImageField(verbose_name='Изображение 1', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    ico1 = models.CharField(verbose_name='Иконка 1', max_length=255, blank=True, null=True, help_text='Вместо изображения пример <i class="fas fa-umbrella fa-fw fa-2x"></i>')
    html1 = HTMLField('Текст', blank=True, null=True)
    pic2 = FilerImageField(verbose_name='Изображение 2', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    ico2 = models.CharField(verbose_name='Иконка 2', max_length=255, blank=True, null=True, help_text='Вместо изображения')
    html2 = HTMLField('Текст', blank=True, null=True)
    pic3 = FilerImageField(verbose_name='Изображение 3', related_name='+', blank=True, null=True,
                           on_delete=models.SET_NULL)
    ico3 = models.CharField(verbose_name='Иконка 3', max_length=255, blank=True, null=True, help_text='Вместо изображения')
    html3 = HTMLField('Текст', blank=True, null=True)