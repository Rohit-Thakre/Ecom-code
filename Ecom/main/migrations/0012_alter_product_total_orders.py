# Generated by Django 4.2.7 on 2023-11-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_product_rating_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_orders',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
