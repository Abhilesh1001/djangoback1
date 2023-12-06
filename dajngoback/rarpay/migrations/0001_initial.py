# Generated by Django 4.2.5 on 2023-11-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tanctiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, verbose_name='Payment Id')),
                ('order_id', models.CharField(max_length=100, verbose_name='Order Id')),
                ('signature', models.CharField(max_length=200, verbose_name='Signature')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('datatime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
