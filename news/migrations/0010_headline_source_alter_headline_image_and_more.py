# Generated by Django 4.2.13 on 2024-05-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_headline_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='source',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.URLField(),
        ),
    ]