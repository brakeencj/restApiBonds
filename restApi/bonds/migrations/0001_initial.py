# Generated by Django 3.2.5 on 2021-07-26 05:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=4, max_digits=13, validators=[django.core.validators.MaxValueValidator(100000000), django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(default='on sale', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bond', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bonds.bond')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bonds.user')),
            ],
        ),
        migrations.AddField(
            model_name='bond',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bonds.user'),
        ),
    ]
