# Generated by Django 3.2.12 on 2022-07-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0006_auto_20220711_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='decompilationrequest',
            name='last_attempted',
            field=models.DateTimeField(default='0001-01-01 00:00:00', editable=False),
        ),
    ]
