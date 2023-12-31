# Generated by Django 4.2.7 on 2023-11-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_order_id_alter_order_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_price',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='max_price',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_orders',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
