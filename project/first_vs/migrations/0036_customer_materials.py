# Generated by Django 4.1.4 on 2023-01-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0035_remove_employees_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='materials',
            field=models.CharField(default='any', max_length=100),
        ),
    ]