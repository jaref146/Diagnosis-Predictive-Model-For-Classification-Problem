# Generated by Django 3.2.6 on 2021-12-03 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0013_alter_sale_book_store_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_info_tabel',
            name='contact_persions_massages',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale_book',
            name='store_post_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 3, 19, 10, 37, 534822)),
        ),
    ]
