# Generated by Django 4.1.4 on 2023-01-11 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0014_bills_customer_ord_amt_customer_payed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='payed',
            new_name='pending_payment',
        ),
    ]
