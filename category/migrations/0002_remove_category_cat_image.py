# Generated by Django 5.1 on 2024-09-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="cat_image",
        ),
    ]
