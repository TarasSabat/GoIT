# Generated by Django 4.2.7 on 2023-11-23 19:10

import app_photo.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_photo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="picture",
            name="path",
            field=models.ImageField(
                upload_to="images", validators=[app_photo.models.validate_file_size]
            ),
        ),
    ]
