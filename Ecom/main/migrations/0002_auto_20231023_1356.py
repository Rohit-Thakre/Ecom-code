# Generated by Django 3.2.18 on 2023-10-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dislikes',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]