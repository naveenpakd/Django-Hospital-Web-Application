# Generated by Django 4.1.6 on 2023-03-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_spec',
            field=models.CharField(max_length=220),
        ),
    ]