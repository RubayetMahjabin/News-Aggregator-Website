# Generated by Django 4.2.13 on 2024-05-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_headline_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='post_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
