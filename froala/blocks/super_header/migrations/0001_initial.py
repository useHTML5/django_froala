# Generated by Django 2.2.7 on 2020-03-11 18:48

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperHeaderConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Название класса')),
                ('icon_class', models.CharField(default='fa fa-cutlery fa-fw', help_text='Можно поставить d-none и тогда полоска будет сплошной', max_length=255, verbose_name='Классы иконки')),
                ('icon_size', models.IntegerField(blank=True, null=True, verbose_name='Размер иконки')),
                ('line_height', models.IntegerField(blank=True, null=True, verbose_name='Высота полоки')),
                ('line_width', models.IntegerField(blank=True, null=True, verbose_name='Ширина полоски')),
                ('color_icon', colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=18, null=True)),
                ('title_class', models.CharField(default='h2', max_length=255, verbose_name='Класс заголовка')),
                ('align', models.CharField(choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], default='center', max_length=255, verbose_name='Выравнивание')),
            ],
        ),
        migrations.CreateModel(
            name='ModelFroalaSuperHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='super_header_modelfroalasuperheader', serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Заголовок')),
                ('conf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='super_header.SuperHeaderConf')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]