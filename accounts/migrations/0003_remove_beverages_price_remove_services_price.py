# Generated by Django 4.2.3 on 2023-07-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_beverages_services"),
    ]

    operations = [
        migrations.RemoveField(model_name="beverages", name="price",),
        migrations.RemoveField(model_name="services", name="price",),
    ]