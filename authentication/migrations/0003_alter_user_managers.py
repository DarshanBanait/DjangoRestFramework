# Generated by Django 5.1.1 on 2024-09-26 18:53

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.models.MyUserManager()),
            ],
        ),
    ]
