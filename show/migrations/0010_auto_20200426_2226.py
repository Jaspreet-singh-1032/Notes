# Generated by Django 3.0 on 2020-04-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
