# Generated by Django 3.0 on 2020-04-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0008_auto_20200425_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=15)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
