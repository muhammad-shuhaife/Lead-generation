# Generated by Django 4.1.4 on 2023-03-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_idcard_mobile_alter_lead_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('emi', models.BooleanField(default=False)),
                ('emi_provider', models.CharField(blank=True, max_length=100)),
                ('bank_loan', models.BooleanField(default=False)),
            ],
        ),
    ]
