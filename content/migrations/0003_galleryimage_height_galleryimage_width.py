# Generated by Django 4.2.7 on 2025-06-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='height',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='width',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
