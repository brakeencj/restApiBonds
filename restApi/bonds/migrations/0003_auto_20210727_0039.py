# Generated by Django 3.2.5 on 2021-07-27 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0002_auto_20210727_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bond',
            old_name='user',
            new_name='seller',
        ),
        migrations.AddField(
            model_name='bond',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='bonds.user'),
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
