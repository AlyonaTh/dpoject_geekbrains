# Generated by Django 5.0.1 on 2024-01-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Product description')),
                ('img', models.ImageField(upload_to='image/shop', verbose_name='Product image')),
                ('link', models.CharField(max_length=200, verbose_name='Affiliate link')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]