# Generated by Django 2.2.2 on 2019-06-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190622_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='owned_prev',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='owned_prev',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='owned_prev',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
