# Generated by Django 5.0 on 2023-12-21 07:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("conversation", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conversationmessage",
            old_name="converstion",
            new_name="conversation",
        ),
    ]
