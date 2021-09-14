# Generated by Django 3.2.7 on 2021-09-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('descuento', models.FloatField(default=0)),
                ('cantMinima', models.IntegerField(default=0)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('codBarra', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.carritocompras')),
            ],
        ),
    ]
