# Generated by Django 5.1.2 on 2024-10-22 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amazon_url', models.URLField(help_text='URL to the Amazon brand page')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('asin', models.CharField(max_length=10, unique=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.URLField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='scrapper.brand')),
            ],
        ),
    ]
