# Generated by Django 3.2.6 on 2022-03-19 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_newfcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newfcompany',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
