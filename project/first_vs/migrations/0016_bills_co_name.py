# Generated by Django 4.1.4 on 2023-01-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0015_rename_payed_customer_pending_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='co_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
