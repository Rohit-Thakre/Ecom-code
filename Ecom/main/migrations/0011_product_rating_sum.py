# Generated by Django 4.2.7 on 2023-11-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_banner_category_alter_banner_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_sum',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
