# Generated by Django 4.1.4 on 2023-01-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0025_alter_employees_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Ssn',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
