# Generated by Django 2.1 on 2018-08-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hidden_description',
            field=models.BooleanField(default=False, help_text='Костыль для фолиантов', verbose_name='Скрытое описание'),
        ),
    ]
