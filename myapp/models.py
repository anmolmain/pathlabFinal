from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField


class AllAppointments(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    PAYMENT_CHOICES = (
        ('cash while specimen taking', 'cash while specimen taking'),
        ('Pre-payment', 'Pre-payment'),
        ('Lab visit', 'Lab visit'),
    )
       
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hospital_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    patient_info = models.TextField(blank=True, null=True)
    
    # Separate fields for each test with boolean value
    cbc = models.BooleanField(default=False)
    bmp = models.BooleanField(default=False)
    lfts = models.BooleanField(default=False)
    lipid_profile = models.BooleanField(default=False)
    thyroid_tests = models.BooleanField(default=False)
    blood_glucose = models.BooleanField(default=False)
    urinalysis = models.BooleanField(default=False)
    stool_analysis = models.BooleanField(default=False)
    coagulation_profile = models.BooleanField(default=False)
    serum_electrolytes = models.BooleanField(default=False)
    crp = models.BooleanField(default=False)
    rheumatoid_factor = models.BooleanField(default=False)
    pt_inr = models.BooleanField(default=False)
    hba1c = models.BooleanField(default=False)
    vitamin_d = models.BooleanField(default=False)
    hiv_antibody = models.BooleanField(default=False)
    hepatitis_panel = models.BooleanField(default=False)
    tumor_marker = models.BooleanField(default=False)
    autoimmune_tests = models.BooleanField(default=False)
    serum_protein = models.BooleanField(default=False)
        
    sample_collection_date = models.DateField()
    sample_collection_time = models.TimeField()
    specimen_type = models.CharField(max_length=255)
    result_required_date = models.DateField()
    
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES,default='cash while specimen taking')
    status = models.CharField(
        max_length=800, 
        choices=[
            ('Booked specimen taking request','Booked specimen taking request'),
            ('Specimen taken successfully','Specimen taken successfully'),
            ('Testing in progress','Testing in progress'),
            ('Tests Completed', 'Tests Completed'), 
            ('Report generation in progress', 'Report generation in progress')
        ], 
        default='Not Started'
    )
    report_url = models.CharField(max_length=255,default='Report will be available to download soon')

    test_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.test_id}"

