# Generated by Django 2.1.3 on 2018-11-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='subContent',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='서브내용'),
        ),
    ]