# Generated by Django 3.2.9 on 2021-11-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='status',
            field=models.CharField(choices=[('New-Arrival', 'New-Arrival'), ('Out-of-Stock', 'Out-of-Stock')], default='New-Arrival', max_length=200),
        ),
    ]
