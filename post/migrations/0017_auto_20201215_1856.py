# Generated by Django 3.1.2 on 2020-12-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20201215_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Underfined', max_length=255),
        ),
    ]
