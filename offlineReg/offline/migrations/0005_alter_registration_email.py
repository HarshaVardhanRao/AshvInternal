# Generated by Django 5.1.1 on 2025-02-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offline", "0004_event_price_alter_registration_registered_on_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="email",
            field=models.CharField(max_length=150),
        ),
    ]
