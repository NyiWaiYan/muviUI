# Generated by Django 4.1.9 on 2023-05-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sofia_auth', '0003_useraccount_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_picture',
            field=models.TextField(null=True),
        ),
    ]
