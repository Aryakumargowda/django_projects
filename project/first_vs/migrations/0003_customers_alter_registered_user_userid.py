# Generated by Django 4.1.4 on 2023-01-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_vs', '0002_login_registered_user_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=40)),
                ('adder', models.TextField(max_length=500)),
                ('gst', models.CharField(max_length=16, unique=True)),
                ('co_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('ord_name', models.CharField(max_length=60)),
                ('ord_number', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='registered_user',
            name='userid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
