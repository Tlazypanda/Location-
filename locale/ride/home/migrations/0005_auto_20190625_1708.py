# Generated by Django 2.2.2 on 2019-06-25 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190625_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='from_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 25, 17, 8, 58, 258602), null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='package',
            field=models.IntegerField(choices=[(1, '4HRS AND 40KMS'), (2, '8HRS AND 80KMS'), (3, '6HRS AND 60KMS'), (4, '10HRS AND 100KMS'), (5, '5HRS AND 50KMS'), (6, '3HRS AND 30KMS'), (7, '12HRS AND 120KMS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ride',
            name='travel_type',
            field=models.IntegerField(choices=[(1, 'LONG DISTANCE'), (2, 'POINT TO POINT'), (3, 'HOURLY RENTAL')], max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.IntegerField(choices=[(1, 'MICRO'), (2, 'MINI'), (3, 'SEDAN'), (4, 'SUV')], max_length=10),
        ),
    ]
