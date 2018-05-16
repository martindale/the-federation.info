# Generated by Django 2.0.3 on 2018-04-28 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thefederation', '0010_add_protocol_to_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='last_success',
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='date',
            field=models.DateField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='thefederation.Node'),
        ),
    ]
