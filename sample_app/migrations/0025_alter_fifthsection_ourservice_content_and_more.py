# Generated by Django 5.0.1 on 2024-03-28 08:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0024_fifthsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fifthsection',
            name='ourservice_content',
            field=ckeditor.fields.RichTextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='ourservice_heading',
            field=ckeditor.fields.RichTextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='ourservice_png',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
    ]
