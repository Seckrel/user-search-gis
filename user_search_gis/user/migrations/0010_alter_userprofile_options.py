# Generated by Django 4.2 on 2023-05-04 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_userprofile_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
