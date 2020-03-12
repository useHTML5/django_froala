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


class LeftIconTextConf(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, default='Стандартный')
    slug = models.SlugField(verbose_name='Название класса', max_length=255, unique=True, default='std')
    classes = models.CharField(verbose_name='Дополнительные классы блока', blank=True, null=True, default='my-2',
                               max_length=255)
    col_ico_classes = models.CharField(verbose_name='Классы иконки', default='col-4 d-flex align-items-center text-primary',
                                       max_length=255)
    col_html_classes = models.CharField(verbose_name='Классы иконки', default='col-8', max_length=255)
    ico_size = models.IntegerField(verbose_name='Размер иконки', default='50')
    color_ico = ColorField(blank=True, null=True, default='')
    align = models.CharField(verbose_name='Положение иконки', default='left', max_length=255, choices=(
        ('left', 'left'),
        ('right', 'right'),
    ))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class ModelFroalaLeftIconText(CMSPlugin):
    conf = models.ForeignKey(LeftIconTextConf, on_delete=models.PROTECT, blank=True, null=True)
    ico = models.CharField(verbose_name='Классы иконки', default='fa fa-cutlery fa-fw', max_length=255)
    classes = models.CharField(verbose_name='Дополнительные классы блока', blank=True, null=True, max_length=255,
                               default="")

    def copy_relations(self, oldinstance):
        self.conf = oldinstance.conf
