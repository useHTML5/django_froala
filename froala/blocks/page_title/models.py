# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField
from solo.models import SingletonModel
from colorfield.fields import ColorField


# from adminsortable.models import SortableMixin
# pic = FilerImageField(verbose_name='Изображение', related_name='+', blank=True, null=True,on_delete=models.SET_NULL)
# html = HTMLField('Текст', blank=True, null=True)

class PageTitleConf(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, default='Стандартный')
    color = ColorField(verbose_name='Цвет наложения', blank=True, null=True, default="")
    blend_mode = models.CharField(verbose_name='Эффект наложения', default='darken', choices=(
        ('normal', 'normal'),
        ('multiply', 'multiply'),
        ('screen', 'screen'),
        ('overlay', 'overlay'),
        ('darken', 'darken'),
        ('lighten', 'lighten'),
        ('color-dodge', 'color-dodge'),
        ('color-burn', 'color-burn'),
        ('hard-light', 'hard-light'),
        ('soft-light', 'soft-light'),
        ('difference', 'difference'),
        ('exclusion', 'exclusion'),
        ('hue', 'hue'),
        ('saturation', 'saturation'),
        ('color', 'color'),
        ('luminosity', 'luminosity')
    ), max_length=255)


class ModelPageTitle(CMSPlugin):
    pic = FilerImageField(verbose_name='Изображение для шапки', blank=True, null=True,
                          on_delete=models.SET_NULL)
    conf = models.ForeignKey(PageTitleConf, on_delete=models.PROTECT, blank=True, null=True)

    def copy_relations(self, oldinstance):
        self.conf = oldinstance.conf
