# Generated by Django 3.2.4 on 2021-06-11 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.IntegerField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('departments', models.CharField(blank=True, max_length=25)),
                ('doctor', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'department',
                'ordering': ('dep_name',),
            },
        ),
        migrations.CreateModel(
            name='docters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapp.department')),
            ],
        ),
    ]
