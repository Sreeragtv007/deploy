# Generated by Django 4.2.6 on 2023-12-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_buyproduct_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]