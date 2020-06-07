# Generated by Django 3.0.7 on 2020-06-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientists', '0004_auto_20200607_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scientists',
            name='field',
        ),
        migrations.AddField(
            model_name='scientists',
            name='field',
            field=models.ManyToManyField(related_name='scientists_field', to='scientists.Field'),
        ),
    ]
