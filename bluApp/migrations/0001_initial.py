# Generated by Django 2.1.4 on 2018-12-12 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50, verbose_name='Apelido do cliente')),
                ('contacto', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('nome_empresa', models.CharField(max_length=60)),
                ('numero_conta', models.CharField(max_length=30)),
                ('data_proposta', models.DateTimeField(auto_now_add=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nome do cliente')),
            ],
        ),
    ]