from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from dasapp.models import Specialization,DoctorReg,Appointment,Page,AddPatient,MedicalHistory,CustomUser,PatientReg
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, get_object_or_404

@login_required(login_url='/')
def ADMINHOME(request):
    doctor_count = DoctorReg.objects.all().count
    specialization_count = Specialization.objects.all().count
    patient_count = AddPatient.objects.all().count
    reguser_count = CustomUser.objects.filter(user_type=3).count
    context = {
        'doctor_count':doctor_count,
        'specialization_count':specialization_count,
        'patient_count':patient_count,
        'reguser_count':reguser_count,

    } 
    return render(request,'admin/adminhome.html',context)

@login_required(login_url='/')
def SPECIALIZATION(request):
    if request.method == "POST":
        specializationname = request.POST.get('specializationname')
        specialization =Specialization(
            sname=specializationname,
        )
        specialization.save()
        messages.success(request,'Specialization  Added Succeesfully!!!')
        return redirect("add_specilizations")
    return render(request,'admin/specialization.html')

@login_required(login_url='/')
def MANAGESPECIALIZATION(request):
    specialization = Specialization.objects.all()
    context = {'specialization':specialization,

    }
    return render(request,'admin/manage_specialization.html',context)

def DELETE_SPECIALIZATION(request,id):
    specialization = Specialization.objects.get(id=id)
    specialization.delete()
    messages.success(request,'Record Delete Succeesfully!!!')
    
    return redirect('manage_specilizations')

login_required(login_url='/')
def UPDATE_SPECIALIZATION(request,id):
    specialization = Specialization.objects.get(id=id)
    
    context = {
         'specialization':specialization,
    }

    return render(request,'admin/update_specialization.html',context)

login_required(login_url='/')

def UPDATE_SPECIALIZATION_DETAILS(request):
        if request.method == 'POST':
          sep_id = request.POST.get('sep_id')
          sname = request.POST.get('sname')
          sepcialization = Specialization.objects.get(id=sep_id) 
          sepcialization.sname = sname
          sepcialization.save()   
          messages.success(request,"Your specialization detail has been updated successfully")
          return redirect('manage_specilizations')
        return render(request, 'admin/update_specialization.html')

@login_required(login_url='/')
def DoctorList(request):
    doctorlist = DoctorReg.objects.all()
    context = {'doctorlist':doctorlist,

    }
    return render(request,'admin/doctor-list.html',context)

def ViewDoctorDetails(request,id):
    doctorlist1=DoctorReg.objects.filter(id=id)
    context={'doctorlist1':doctorlist1

    }

    return render(request,'admin/doctor-details.html',context)

def View_DOCPatient(request,id):
    patde = AddPatient.objects.filter(doctor_id=id)
    context={
        'patde':patde
    }
    return render(request, 'admin/views_docpatient.html',context)


@login_required(login_url='/')
def ViewCheckAddPatient(request,id):    
    patient_data = AddPatient.objects.get(id =id) 
    medrec_data = MedicalHistory.objects.filter(pat_id =id)    
    context = {
        
        "pd":patient_data,
        "mrd":medrec_data,
    }
    return render(request,'admin/update_patientmdrec.html',context)

def ViewDoctorAppointmentList(request,id):
    patientdetails=Appointment.objects.filter(doctor_id=id)
    context={'patientdetails':patientdetails

    }

    return render(request,'admin/doctor_appointment_list.html',context)

def ViewPatientDetails(request,id):
    patientdetails=Appointment.objects.filter(id=id)
    context={'patientdetails':patientdetails

    }

    return render(request,'admin/patient_appointment_details.html',context)

def Search_Doctor(request):
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where email or mobilenumber contains the query
            searchdoc = DoctorReg.objects.filter(mobilenumber__icontains=query) | DoctorReg.objects.filter(admin__first_name__icontains=query) | DoctorReg.objects.filter(admin__last_name__icontains=query)
            messages.info(request, "Search against " + query)
            return render(request, 'admin/search-doctor.html', {'searchdoc': searchdoc, 'query': query})
        else:
            print("No Record Found")
            return render(request, 'admin/search-doctor.html', {})

def Doctor_Between_Date_Report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    doctor = []

    if start_date and end_date:
        # Validate the date inputs
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'admin/doctor-between-date.html', {'doctor': doctor, 'error_message': 'Invalid date format'})

        # Filter visitors between the given date range
        doctor = DoctorReg.objects.filter(regdate_at__range=(start_date, end_date))

    return render(request, 'admin/doctor-between-date.html', {'doctor': doctor,'start_date':start_date,'end_date':end_date})


@login_required(login_url='/')
def WEBSITE_UPDATE(request):
    page = Page.objects.all()
    context = {"page":page,

    }
    return render(request,'admin/website.html',context)

@login_required(login_url='/')
def UPDATE_WEBSITE_DETAILS(request):
    if request.method == 'POST':
          web_id = request.POST.get('web_id')
          pagetitle = request.POST['pagetitle']
          address = request.POST['address']
          aboutus = request.POST['aboutus']
          email = request.POST['email']
          mobilenumber = request.POST['mobilenumber']
          page =Page.objects.get(id=web_id)
          page.pagetitle = pagetitle
          page.address = address
          page.aboutus = aboutus
          page.email = email
          page.mobilenumber = mobilenumber
          page.save()
          messages.success(request,"Your website detail has been updated successfully")
          return redirect('website_update')
    return render(request,'admin/website.html')

@login_required(login_url='/')
def RegUsersDetails(request):
    regusers = PatientReg.objects.all()
    context = {"regusers":regusers}
    return render(request,'admin/reg-users.html',context)

@login_required(login_url='/')
def DELETE_REGUSERS(request, id):
    try:
        patreg = get_object_or_404(PatientReg, id=id)
        custom_user = patreg.admin  # Access the related CustomUser
        patreg.delete()  # This will also delete the associated CustomUser because of the on_delete=models.CASCADE
        custom_user.delete()
        messages.success(request, 'Record deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting record: {e}')
    return redirect('regusers')

@login_required(login_url='/')
def Reg_User_Appoinments(request,id):
    pat_admin = PatientReg.objects.get(id=id)
    userapptdetails = Appointment.objects.filter(pat_id=pat_admin)
    context = {
        'vah':userapptdetails
    }
    return render(request, 'admin/reg_users_appointment.html', context)



