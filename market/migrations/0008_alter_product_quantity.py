# Generated by Django 5.1.7 on 2025-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_alter_order_total_price_alter_orderitem_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
