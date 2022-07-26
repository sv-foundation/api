# Generated by Django 4.0.6 on 2022-07-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstag',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
