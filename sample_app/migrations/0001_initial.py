# Generated by Django 5.0.1 on 2024-02-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emailid', models.EmailField(max_length=254)),
                ('ourservices', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
