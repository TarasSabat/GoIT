# Generated by Django 3.2.12 on 2024-05-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
