# Generated by Django 4.0.3 on 2022-04-09 14:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0003_alter_inquiry_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]