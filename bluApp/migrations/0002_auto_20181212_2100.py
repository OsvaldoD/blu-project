# Generated by Django 2.1.4 on 2018-12-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='data_proposta',
            field=models.DateTimeField(),
        ),
    ]