# Generated by Django 3.2.6 on 2021-08-26 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('localisation', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_django.ressource')),
            ],
        ),
    ]
