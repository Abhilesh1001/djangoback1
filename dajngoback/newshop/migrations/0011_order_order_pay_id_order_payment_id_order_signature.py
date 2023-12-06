# Generated by Django 4.2.5 on 2023-12-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshop', '0010_product_qty_product_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_pay_id',
            field=models.CharField(default='', max_length=100, verbose_name='Order Id'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default='', max_length=100, verbose_name='Payment Id'),
        ),
        migrations.AddField(
            model_name='order',
            name='signature',
            field=models.CharField(default='', max_length=200, verbose_name='Signature'),
        ),
    ]
