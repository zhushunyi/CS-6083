# Generated by Django 4.0.4 on 2022-05-09 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_individualinfo_password_individualinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualinfo',
            name='password',
            field=models.CharField(default='2022050914133467', max_length=64, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='individualinfo',
            name='username',
            field=models.CharField(default='2022050914136099', max_length=32, verbose_name='username'),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vclass', models.SmallIntegerField(choices=[(1, 'small'), (2, 'mid-size'), (3, 'luxury'), (4, 'SUV'), (5, 'premium'), (6, 'special'), (7, 'van')], verbose_name='Class')),
                ('make', models.SmallIntegerField(choices=[(1, 'Mercedes-Benz'), (2, 'Audi'), (3, 'GMC'), (4, 'Nissan'), (5, 'Avalon'), (6, 'Blazer'), (7, 'Cayenne Coupe')], verbose_name='Make')),
                ('year', models.DateField(verbose_name='Year')),
                ('VIN', models.CharField(max_length=10, verbose_name='VIN')),
                ('LPN', models.CharField(max_length=10, verbose_name='LPN')),
                ('daily_rate', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Daily Rate')),
                ('extra_rate', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Extra Rate')),
                ('limit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Limit')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.office')),
            ],
        ),
    ]
