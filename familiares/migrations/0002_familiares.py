# Generated by Django 4.1 on 2022-09-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fec_nac', models.DateField()),
                ('relacion', models.CharField(max_length=40)),
            ],
        ),
    ]
