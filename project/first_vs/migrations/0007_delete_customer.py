# Generated by Django 4.1.4 on 2023-01-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0006_alter_customer_email_alter_customer_gst'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]