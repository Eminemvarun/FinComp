# Generated by Django 5.0.1 on 2024-04-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='vendor/default.jpg', upload_to='profile_pics'),
        ),
    ]
