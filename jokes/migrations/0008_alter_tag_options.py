# Generated by Django 4.1.2 on 2022-11-19 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0007_tag_joke_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
    ]