# Generated by Django 4.2.11 on 2024-05-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
