# Generated by Django 4.1.7 on 2023-04-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-06-16'),
            preserve_default=False,
        ),
    ]
