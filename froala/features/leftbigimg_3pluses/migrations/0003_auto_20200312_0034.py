# Generated by Django 2.2.7 on 2020-03-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leftbigimg_3pluses', '0002_auto_20200311_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelleftbigimg3pluses',
            name='ico1',
            field=models.CharField(blank=True, help_text='Вместо изображения пример <i class="fas fa-umbrella fa-fw fa-2x"></i>', max_length=255, null=True, verbose_name='Иконка 1'),
        ),
    ]
