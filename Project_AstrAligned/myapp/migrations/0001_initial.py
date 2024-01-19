# Generated by Django 5.0.1 on 2024-01-19 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ZodiacSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.CharField(max_length=20)),
                ('short_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AccountHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empathy', models.FloatField(default=0)),
                ('resilience', models.FloatField(default=0)),
                ('integrity', models.FloatField(default=0)),
                ('adaptability', models.FloatField(default=0)),
                ('open_mindedness', models.FloatField(default=0)),
                ('responsibility', models.FloatField(default=0)),
                ('confidence', models.FloatField(default=0)),
                ('perseverance', models.FloatField(default=0)),
                ('kindness', models.FloatField(default=0)),
                ('curiosity', models.FloatField(default=0)),
                ('loyalty', models.FloatField(default=0)),
                ('zodiac_sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.zodiacsign')),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(max_length=15)),
                ('polarity', models.CharField(max_length=15)),
                ('modality', models.CharField(max_length=15)),
                ('ruling_house_one', models.CharField(max_length=15)),
                ('ruling_house_two', models.CharField(max_length=15)),
                ('zodiac_sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.zodiacsign')),
            ],
        ),
    ]