# Generated by Django 4.1.7 on 2023-10-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_buyproduct_address_buyproduct_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproduct',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]