# Generated by Django 5.0.1 on 2024-06-11 12:06

import ckeditor.fields
import sample_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0066_paidpromotioncontentimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footersection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(default='', max_length=255)),
                ('logo', models.ImageField(default='', upload_to=sample_app.models.get_image_filename)),
            ],
            options={
                'verbose_name_plural': 'Footersection',
            },
        ),
    ]
