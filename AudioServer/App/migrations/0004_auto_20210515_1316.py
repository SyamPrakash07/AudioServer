# Generated by Django 3.2.3 on 2021-05-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210515_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Song_ID',
            field=models.IntegerField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='Uploaded_Time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.FloatField(max_length=20),
        ),
    ]
