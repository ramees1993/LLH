# Generated by Django 5.0.4 on 2024-07-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_remove_contact_phone_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
