# Generated by Django 3.1.3 on 2020-11-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake', '0008_auto_20201118_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]