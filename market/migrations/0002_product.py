# Generated by Django 4.2.20 on 2025-03-18 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.PositiveIntegerField(default=1)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='market.market')),
            ],
        ),
    ]
