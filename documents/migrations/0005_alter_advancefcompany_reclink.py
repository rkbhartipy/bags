# Generated by Django 3.2.6 on 2022-03-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_advancefcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancefcompany',
            name='RecLink',
            field=models.CharField(max_length=200),
        ),
    ]