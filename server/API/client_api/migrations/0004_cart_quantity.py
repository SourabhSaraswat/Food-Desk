# Generated by Django 3.0.6 on 2020-08-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_api', '0003_remove_cart_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=1),
        ),
    ]
