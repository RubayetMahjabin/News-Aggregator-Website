# Generated by Django 4.2.13 on 2024-05-29 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_headline_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='date',
        ),
    ]
