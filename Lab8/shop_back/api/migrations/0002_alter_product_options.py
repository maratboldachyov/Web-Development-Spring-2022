# Generated by Django 4.0.3 on 2022-04-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-price',)},
        ),
    ]
