# Generated by Django 4.2.7 on 2023-12-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='slug',
            field=models.SlugField(max_length=249),
        ),
    ]