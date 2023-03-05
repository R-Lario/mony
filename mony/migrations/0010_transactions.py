# Generated by Django 4.1.3 on 2023-02-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mony', '0009_alter_agreements_bank_name_alter_banks_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('transaction_id', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('currency', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]