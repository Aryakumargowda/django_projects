# Generated by Django 4.1.4 on 2023-01-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0010_bills_customer_ord_amt_customer_payed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ord_amt',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='payed',
            field=models.CharField(max_length=20),
        ),
    ]