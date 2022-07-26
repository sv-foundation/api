# Generated by Django 4.0.6 on 2022-07-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_paymentsystemcurrency_remove_paymentdetails_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentdetails',
            options={'ordering': ['order', '-created'], 'verbose_name_plural': 'payment details'},
        ),
        migrations.AlterModelOptions(
            name='paymentsystemcurrency',
            options={'ordering': ['order'], 'verbose_name_plural': 'payment system currencies'},
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='order',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='paymentsystemcurrency',
            name='order',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
