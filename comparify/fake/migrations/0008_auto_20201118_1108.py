# Generated by Django 3.1.3 on 2020-11-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake', '0007_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
    ]
