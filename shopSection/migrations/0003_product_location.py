# Generated by Django 4.1.4 on 2023-02-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopSection', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
