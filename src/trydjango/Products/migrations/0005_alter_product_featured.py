# Generated by Django 5.0.1 on 2024-01-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
