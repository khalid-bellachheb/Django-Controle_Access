# Generated by Django 3.1.1 on 2020-10-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ttn', '0002_auto_20200920_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_ttn',
            name='device_id',
            field=models.CharField(default=-1, max_length=15),
            preserve_default=False,
        ),
    ]