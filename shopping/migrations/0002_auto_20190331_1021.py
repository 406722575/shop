# Generated by Django 2.0.5 on 2019-03-31 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='product_picture',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_picture',
            new_name='picture',
        ),
    ]
