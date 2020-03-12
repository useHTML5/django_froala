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


class SuperHeaderConf(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='Название класса', max_length=255, unique=True)
    icon_class = models.CharField(verbose_name='Классы иконки', default='fa fa-cutlery fa-fw', max_length=255,
                                  help_text='Можно поставить d-none и тогда полоска будет сплошной')
    icon_size = models.IntegerField(verbose_name='Размер иконки', blank=True, null=True)
    line_height = models.IntegerField(verbose_name='Высота полоки', blank=True, null=True)
    line_width = models.IntegerField(verbose_name='Ширина полоски', blank=True, null=True)
    color_icon = ColorField(blank=True, null=True)
    color_line = ColorField(blank=True, null=True)
    title_class = models.CharField(verbose_name='Класс заголовка', default='h2', max_length=255)
    align = models.CharField(verbose_name='Выравнивание', default='center', max_length=255, choices=(
        ('left', 'left'),
        ('right', 'right'),
        ('center', 'center'),
    ))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class ModelFroalaSuperHeader(CMSPlugin):
    title = models.TextField(verbose_name='Заголовок', blank=True, null=True)
    classes = models.TextField(verbose_name='Дополнительные классы блока', blank=True, null=True)
    conf = models.ForeignKey(SuperHeaderConf, on_delete=models.PROTECT, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def copy_relations(self, oldinstance):
        self.conf = oldinstance.conf
