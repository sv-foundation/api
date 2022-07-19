# Generated by Django 4.0.6 on 2022-07-19 15:51

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('name_uk', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_pl', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(upload_to='fond_documents/')),
                ('file_uk', models.FileField(null=True, upload_to='fond_documents/')),
                ('file_en', models.FileField(null=True, upload_to='fond_documents/')),
                ('file_pl', models.FileField(null=True, upload_to='fond_documents/')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('currency_code', models.CharField(choices=[('AED', 'AED'), ('AFN', 'AFN'), ('ALL', 'ALL'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BYR', 'BYR'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CZK', 'CZK'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ETB', 'ETB'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GMD', 'GMD'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('ISK', 'ISK'), ('JEP', 'JEP'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LBP', 'LBP'), ('LKR', 'LKR'), ('LTL', 'LTL'), ('LVL', 'LVL'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('NZD', 'NZD'), ('OMR', 'OMR'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RON', 'RON'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SCR', 'SCR'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('STD', 'STD'), ('SYP', 'SYP'), ('THB', 'THB'), ('TND', 'TND'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UGX', 'UGX'), ('USD', 'USD'), ('UYU', 'UYU'), ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('XAF', 'XAF'), ('XBT', 'XBT'), ('XCD', 'XCD'), ('XOF', 'XOF'), ('XPF', 'XPF'), ('ZAR', 'ZAR'), ('ZMW', 'ZMW')], default='UAH', max_length=5, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255, null=True)),
                ('card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('iban', models.CharField(max_length=40, verbose_name='IBAN')),
                ('bic', models.CharField(blank=True, max_length=20, null=True, verbose_name='BIC')),
                ('fund_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank', models.CharField(blank=True, max_length=255, null=True)),
                ('corespondent_banks', models.TextField(blank=True, null=True)),
                ('payment_purpose', models.CharField(blank=True, max_length=255, null=True)),
                ('is_visible', models.BooleanField(default=True, help_text='Is visible on website')),
            ],
            options={
                'verbose_name_plural': 'payment details',
            },
        ),
    ]