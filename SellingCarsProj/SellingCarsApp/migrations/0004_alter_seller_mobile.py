# Generated by Django 3.2.5 on 2022-05-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellingCarsApp', '0003_alter_seller_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]