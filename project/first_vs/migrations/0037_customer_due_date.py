# Generated by Django 4.1.4 on 2023-01-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0036_customer_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
