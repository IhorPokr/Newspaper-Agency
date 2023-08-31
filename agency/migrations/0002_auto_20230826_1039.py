# Generated by Django 4.2.4 on 2023-08-26 15:39
from django.db import migrations
from django.db.migrations import RunPython


def func(apps, schema_editor):
    from django.core.management import call_command
    call_command('loaddata', 'fixture_data')


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0001_initial"),
    ]

    operations = [
        RunPython(reverse_func, func),
    ]
