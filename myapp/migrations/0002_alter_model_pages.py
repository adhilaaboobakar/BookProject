# Generated by Django 5.0.1 on 2024-01-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='pages',
            field=models.PositiveIntegerField(),
        ),
    ]
