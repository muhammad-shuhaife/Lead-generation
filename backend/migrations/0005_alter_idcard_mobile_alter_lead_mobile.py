# Generated by Django 4.1.4 on 2023-03-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_idcard_lead_source_alter_lead_mobile_alter_lead_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='Mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='Mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
