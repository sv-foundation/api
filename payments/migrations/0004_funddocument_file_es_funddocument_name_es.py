# Generated by Django 4.0.6 on 2022-09-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_paymentdetails_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funddocument',
            name='file_es',
            field=models.FileField(null=True, upload_to='fond_documents/'),
        ),
        migrations.AddField(
            model_name='funddocument',
            name='name_es',
            field=models.CharField(max_length=255, null=True),
        ),
    ]