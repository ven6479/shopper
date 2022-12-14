# Generated by Django 4.1.4 on 2022-12-13 00:25

from django.db import migrations
import testshop.fields
import testshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('testshop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=testshop.fields.WEBPField(default=None, upload_to=testshop.models.image_folder),
        ),
    ]
