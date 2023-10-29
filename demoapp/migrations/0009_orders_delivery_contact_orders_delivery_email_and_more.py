# Generated by Django 4.2.4 on 2023-10-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_orders_order_number_alter_orders_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='delivery_contact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
