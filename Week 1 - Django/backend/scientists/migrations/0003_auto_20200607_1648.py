# Generated by Django 3.0.7 on 2020-06-07 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scientists', '0002_auto_20200607_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scientists',
            name='field',
        ),
        migrations.AddField(
            model_name='scientists',
            name='field_new',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='scientists_field', to='scientists.Field'),
        ),
    ]
