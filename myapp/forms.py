from django import forms
from .models import AllAppointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AllAppointments
        fields = [
            'name', 'dob', 'gender', 'hospital_name', 'contact', 'email',
            'address', 'patient_info', 'cbc', 'bmp', 'lfts', 'lipid_profile',
            'thyroid_tests', 'blood_glucose', 'urinalysis', 'stool_analysis',
            'coagulation_profile', 'serum_electrolytes', 'crp',
            'rheumatoid_factor', 'pt_inr', 'hba1c', 'vitamin_d', 'hiv_antibody',
            'hepatitis_panel', 'tumor_marker', 'autoimmune_tests', 'serum_protein',
            'sample_collection_date', 'sample_collection_time', 'specimen_type',
            'result_required_date'
        ]

    # Customizing labels and widgets
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['dob'].label = "Date of Birth"
        self.fields['gender'].label = "Gender"
        self.fields['hospital_name'].label = "Hospital Name"
        self.fields['contact'].label = "Contact"
        self.fields['email'].label = "Email"
        self.fields['address'].label = "Address"
        self.fields['patient_info'].label = "Patient Information"
        
        # Test Fields
        self.fields['cbc'].label = "CBC"
        self.fields['bmp'].label = "BMP"
        self.fields['lfts'].label = "LFTs"
        self.fields['lipid_profile'].label = "Lipid Profile"
        self.fields['thyroid_tests'].label = "Thyroid Tests"
        self.fields['blood_glucose'].label = "Blood Glucose"
        self.fields['urinalysis'].label = "Urinalysis"
        self.fields['stool_analysis'].label = "Stool Analysis"
        self.fields['coagulation_profile'].label = "Coagulation Profile"
        self.fields['serum_electrolytes'].label = "Serum Electrolytes"
        self.fields['crp'].label = "CRP"
        self.fields['rheumatoid_factor'].label = "Rheumatoid Factor"
        self.fields['pt_inr'].label = "PT/INR"
        self.fields['hba1c'].label = "HbA1c"
        self.fields['vitamin_d'].label = "Vitamin D"
        self.fields['hiv_antibody'].label = "HIV Antibody"
        self.fields['hepatitis_panel'].label = "Hepatitis Panel"
        self.fields['tumor_marker'].label = "Tumor Marker"
        self.fields['autoimmune_tests'].label = "Autoimmune Tests"
        self.fields['serum_protein'].label = "Serum Protein"
        
        self.fields['sample_collection_date'].label = "Sample Collection Date"
        self.fields['sample_collection_time'].label = "Sample Collection Time"
        self.fields['specimen_type'].label = "Specimen Type"
        self.fields['result_required_date'].label = "Result Required Date"
