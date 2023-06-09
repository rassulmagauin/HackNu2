# Generated by Django 4.2 on 2023-04-15 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('building_number', models.CharField(blank=True, max_length=50)),
                ('apartment', models.CharField(blank=True, max_length=50)),
                ('entry', models.CharField(blank=True, max_length=50)),
                ('floor', models.CharField(blank=True, max_length=50)),
                ('corpus', models.CharField(blank=True, max_length=50)),
                ('jk', models.CharField(blank=True, max_length=50)),
                ('additional', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=255)),
                ('IIN', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('aIIN', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.address')),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='courier.courier')),
            ],
        ),
    ]
