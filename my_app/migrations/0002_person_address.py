# Generated by Django 4.2.2 on 2023-07-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default='', max_length=200),
        ),
    ]
