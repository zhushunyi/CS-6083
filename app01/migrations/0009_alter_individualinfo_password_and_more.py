# Generated by Django 4.0.4 on 2022-05-10 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_alter_individualinfo_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualinfo',
            name='password',
            field=models.CharField(default='2022051002419594', max_length=64, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='individualinfo',
            name='username',
            field=models.CharField(default='2022051002417303', max_length=32, verbose_name='username'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentDate', models.DateField(verbose_name='Payment Date')),
                ('PaymentMethod', models.SmallIntegerField(choices=[(1, 'credit'), (2, 'debit')], verbose_name='Payment Method')),
                ('CardNum', models.CharField(max_length=10, verbose_name='Card Number')),
                ('InvoiceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.invoice')),
            ],
        ),
    ]