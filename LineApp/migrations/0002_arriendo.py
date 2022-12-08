# Generated by Django 4.1.3 on 2022-12-08 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LineApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('idArriendo', models.AutoField(primary_key=True, serialize=False, verbose_name='id arriendo')),
                ('titular', models.IntegerField(verbose_name='Id del titular')),
                ('arrendatario', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='arrendatario')),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LineApp.estacionamiento')),
            ],
        ),
    ]
