# Generated by Django 3.2.4 on 2021-07-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0004_rename_img_items_imag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(),
        ),
    ]
