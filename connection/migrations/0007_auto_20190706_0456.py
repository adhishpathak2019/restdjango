# Generated by Django 2.2.3 on 2019-07-06 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0006_auto_20190705_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connections',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
