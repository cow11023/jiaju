# Generated by Django 4.1.4 on 2023-06-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='current_fan_speed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='current_temperature',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='fan_speed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='temperature',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
