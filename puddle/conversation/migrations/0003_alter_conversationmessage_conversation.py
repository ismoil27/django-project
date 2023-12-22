# Generated by Django 5.0 on 2023-12-22 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conversation", "0002_rename_converstion_conversationmessage_conversation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversationmessage",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="conversation.conversation",
            ),
        ),
    ]