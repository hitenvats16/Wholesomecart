# Generated by Django 4.0.5 on 2022-06-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Date_Ordered',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Time_Ordered',
            field=models.TimeField(auto_now=True),
        ),
    ]
