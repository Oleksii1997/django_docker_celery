# Generated by Django 3.2.4 on 2021-06-17 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт: ', 'verbose_name_plural': 'Контакти'},
        ),
    ]
