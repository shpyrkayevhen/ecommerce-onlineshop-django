# Generated by Django 3.1 on 2022-12-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20221205_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]