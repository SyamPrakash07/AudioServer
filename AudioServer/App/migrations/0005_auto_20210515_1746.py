# Generated by Django 3.2.3 on 2021-05-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210515_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='duration',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.FloatField(),
        ),
    ]