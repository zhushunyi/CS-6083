# Generated by Django 4.0.4 on 2022-05-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_corporationuser_individualinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='user name')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
            ],
        ),
    ]
