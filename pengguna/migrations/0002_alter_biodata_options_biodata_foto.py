# Generated by Django 5.2 on 2025-05-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biodata',
            options={'verbose_name_plural': '1. Biodata'},
        ),
        migrations.AddField(
            model_name='biodata',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pengguna'),
        ),
    ]
