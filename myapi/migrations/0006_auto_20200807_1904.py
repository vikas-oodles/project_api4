# Generated by Django 3.1 on 2020-08-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20200807_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DOB'),
        ),
    ]
