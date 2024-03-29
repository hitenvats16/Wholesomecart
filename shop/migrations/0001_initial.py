# Generated by Django 4.0.5 on 2022-06-16 16:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Prod_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(default='', max_length=50)),
                ('Discription', models.TextField()),
                ('Publish_Data', models.DateField()),
                ('Catagory', models.CharField(default='', max_length=50)),
                ('Sub_Catagory', models.CharField(default='', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
