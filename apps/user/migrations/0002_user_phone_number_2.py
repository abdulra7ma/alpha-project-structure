# Generated by Django 4.1b1 on 2022-07-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number_2",
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
