# Generated by Django 4.1.4 on 2022-12-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testshop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='slug'),
        ),
    ]