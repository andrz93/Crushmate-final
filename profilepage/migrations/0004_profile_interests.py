# Generated by Django 5.0.14 on 2025-05-31 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profilepage", "0003_profilephoto_is_main"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="interests",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
