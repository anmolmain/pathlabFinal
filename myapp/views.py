from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import date
from django.core.paginator import Paginator
from django.http import HttpResponse
from myapp.models import AllAppointments
from .forms import AppointmentForm


# Home view0
def home(request):
    try:
        return render(request, "home.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")
# Home view0
def formsubmitted(request):
    try:
        return render(request, "formsubmitted.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

def about(request):
    try:
        return render(request, "about.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

# Login view to login user
def login(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Invalid Credential")
                return redirect("login")
        else:
            return render(request, "login.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("login")

# Register view to register user
def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exist")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    return redirect("login")
            else:
                messages.info(request, "Password not matches")
                return redirect("register")
        else:
            return render(request, "register.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("register")

# Logout view to logout user
def logout(request):
    try:
        auth.logout(request)
        return redirect("/")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

# Book appointment
def bookappointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            hospital_name = form.cleaned_data['hospital_name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            patient_info = form.cleaned_data['patient_info']
            
            # Test Fields
            cbc = form.cleaned_data['cbc']
            bmp = form.cleaned_data['bmp']
            lfts = form.cleaned_data['lfts']
            lipid_profile = form.cleaned_data['lipid_profile']
            thyroid_tests = form.cleaned_data['thyroid_tests']
            blood_glucose = form.cleaned_data['blood_glucose']
            urinalysis = form.cleaned_data['urinalysis']
            stool_analysis = form.cleaned_data['stool_analysis']
            coagulation_profile = form.cleaned_data['coagulation_profile']
            serum_electrolytes = form.cleaned_data['serum_electrolytes']
            crp = form.cleaned_data['crp']
            rheumatoid_factor = form.cleaned_data['rheumatoid_factor']
            pt_inr = form.cleaned_data['pt_inr']
            hba1c = form.cleaned_data['hba1c']
            vitamin_d = form.cleaned_data['vitamin_d']
            hiv_antibody = form.cleaned_data['hiv_antibody']
            hepatitis_panel = form.cleaned_data['hepatitis_panel']
            tumor_marker = form.cleaned_data['tumor_marker']
            autoimmune_tests = form.cleaned_data['autoimmune_tests']
            serum_protein = form.cleaned_data['serum_protein']
            
            sample_collection_date = form.cleaned_data['sample_collection_date']
            sample_collection_time = form.cleaned_data['sample_collection_time']
            specimen_type = form.cleaned_data['specimen_type']
            result_required_date = form.cleaned_data['result_required_date']

            # Create a new AllAppointments object and save it to the database
            appointment = AllAppointments(
                name=name,
                dob=dob,
                gender=gender,
                hospital_name=hospital_name,
                contact=contact,
                email=email,
                address=address,
                patient_info=patient_info,
                cbc=cbc,
                bmp=bmp,
                lfts=lfts,
                lipid_profile=lipid_profile,
                thyroid_tests=thyroid_tests,
                blood_glucose=blood_glucose,
                urinalysis=urinalysis,
                stool_analysis=stool_analysis,
                coagulation_profile=coagulation_profile,
                serum_electrolytes=serum_electrolytes,
                crp=crp,
                rheumatoid_factor=rheumatoid_factor,
                pt_inr=pt_inr,
                hba1c=hba1c,
                vitamin_d=vitamin_d,
                hiv_antibody=hiv_antibody,
                hepatitis_panel=hepatitis_panel,
                tumor_marker=tumor_marker,
                autoimmune_tests=autoimmune_tests,
                serum_protein=serum_protein,
                sample_collection_date=sample_collection_date,
                sample_collection_time=sample_collection_time,
                specimen_type=specimen_type,
                result_required_date=result_required_date
            )
            appointment.save()
            return redirect('formsubmitted')  # Redirect to a success page
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bookappointment.html', context)

def appointment_success(request):
    return render(request, 'about.html')

def viewstatus(request):
    status = None
    report_url = None  # Initialize with a default value

    if request.method == 'POST':
        test_id = request.POST.get('test_id')
        
        # Fetch status from database based on test_id
        appointment = AllAppointments.objects.filter(test_id=test_id).first()
        
        if appointment:
            status = appointment.status
            report_url = appointment.report_url
        else:
            status = "Not found"

    context = {
        'status': status,
        'report_url': report_url,
        'test_id': request.POST.get('test_id', ''),
    }
    return render(request, 'viewstatus.html', context)

def alltest(request):
    # Fetch all appointments for the current logged-in user
    appointments = AllAppointments.objects.filter(patient_info=request.user.username)
    
    context = {
        'appointments': appointments
    }
    print(context)
    
    return render(request, 'alltest.html', context)