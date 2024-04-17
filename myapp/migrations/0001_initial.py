# Generated by Django 5.0.4 on 2024-04-17 17:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('hospital_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('patient_info', models.TextField(blank=True, null=True)),
                ('cbc', models.BooleanField(default=False)),
                ('bmp', models.BooleanField(default=False)),
                ('lfts', models.BooleanField(default=False)),
                ('lipid_profile', models.BooleanField(default=False)),
                ('thyroid_tests', models.BooleanField(default=False)),
                ('blood_glucose', models.BooleanField(default=False)),
                ('urinalysis', models.BooleanField(default=False)),
                ('stool_analysis', models.BooleanField(default=False)),
                ('coagulation_profile', models.BooleanField(default=False)),
                ('serum_electrolytes', models.BooleanField(default=False)),
                ('crp', models.BooleanField(default=False)),
                ('rheumatoid_factor', models.BooleanField(default=False)),
                ('pt_inr', models.BooleanField(default=False)),
                ('hba1c', models.BooleanField(default=False)),
                ('vitamin_d', models.BooleanField(default=False)),
                ('hiv_antibody', models.BooleanField(default=False)),
                ('hepatitis_panel', models.BooleanField(default=False)),
                ('tumor_marker', models.BooleanField(default=False)),
                ('autoimmune_tests', models.BooleanField(default=False)),
                ('serum_protein', models.BooleanField(default=False)),
                ('sample_collection_date', models.DateField()),
                ('sample_collection_time', models.TimeField()),
                ('specimen_type', models.CharField(max_length=255)),
                ('result_required_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('cash while specimen taking', 'cash while specimen taking'), ('Pre-payment', 'Pre-payment'), ('Lab visit', 'Lab visit')], default='cash while specimen taking', max_length=50)),
                ('status', models.CharField(choices=[('Booked specimen taking request', 'Booked specimen taking request'), ('Specimen taken successfully', 'Specimen taken successfully'), ('Testing in progress', 'Testing in progress'), ('Tests Completed', 'Tests Completed'), ('Report generation in progress', 'Report generation in progress')], default='Not Started', max_length=800)),
                ('report_url', models.CharField(default='Report will be available to download soon', max_length=255)),
                ('test_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]