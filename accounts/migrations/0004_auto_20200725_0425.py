# Generated by Django 3.0.8 on 2020-07-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200725_0425'),
        ('accounts', '0003_auto_20200724_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='product_list',
            field=models.ManyToManyField(to='products.Products'),
        ),
    ]