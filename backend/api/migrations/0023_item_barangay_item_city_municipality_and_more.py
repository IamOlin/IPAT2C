# Generated by Django 5.0.4 on 2024-07-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_item_pagibig_no_item_philhealth_no_item_sss_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='barangay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='city_municipality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='father_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='father_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='father_middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='mother_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='mother_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='mother_middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]