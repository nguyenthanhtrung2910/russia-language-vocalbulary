# Generated by Django 5.0.6 on 2024-05-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocalbulary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocalbulary',
            name='word_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]