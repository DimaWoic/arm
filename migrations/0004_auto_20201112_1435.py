# Generated by Django 3.0 on 2020-11-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0003_auto_20201112_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numcar',
            options={'verbose_name': 'номер машины', 'verbose_name_plural': 'номера машины'},
        ),
        migrations.AlterField(
            model_name='numcar',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Номер машины'),
        ),
    ]
