# Generated by Django 3.1.4 on 2020-12-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20201209_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
