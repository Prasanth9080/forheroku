# Generated by Django 5.0.1 on 2024-02-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0008_delete_emailsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='recipient_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]