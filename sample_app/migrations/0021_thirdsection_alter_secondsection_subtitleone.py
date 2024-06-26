# Generated by Django 5.0.1 on 2024-03-27 10:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0020_secondsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thirdsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='secondsection',
            name='subtitleone',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]
