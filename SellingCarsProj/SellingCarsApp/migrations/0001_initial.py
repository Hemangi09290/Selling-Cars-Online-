# Generated by Django 3.2.5 on 2022-05-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('make', models.IntegerField()),
                ('model', models.CharField(max_length=200)),
                ('year', models.DateTimeField()),
                ('condition', models.CharField(choices=[('poor', 'Poor'), ('fair', 'Fair'), ('good', 'Good'), ('excellent', 'Excellent')], max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('is_sold', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('password', models.CharField(help_text='Enter 8 digits password', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=200)),
                ('is_makecar_avail', models.BooleanField(default=False)),
            ],
        ),
    ]
