# Generated by Django 3.2.9 on 2021-11-29 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='MainCategory')),
                ('info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='subCategory')),
                ('info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Product')),
                ('og_price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('sell_price', models.IntegerField(default=0)),
                ('info', models.TextField()),
                ('mcate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.maincategorymodel')),
                ('scate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subcategorymodel')),
            ],
        ),
    ]
