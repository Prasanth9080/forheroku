# Generated by Django 5.0.1 on 2024-02-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0003_alter_contactform_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_backend', models.CharField(default='', max_length=255)),
                ('email_host', models.CharField(default='', max_length=255)),
                ('email_port', models.IntegerField(default=587)),
                ('email_host_user', models.CharField(default='', max_length=255)),
                ('email_host_password', models.CharField(default='', max_length=255)),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_use_ssl', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Contact Form', 'verbose_name_plural': 'UserData'},
        ),
    ]