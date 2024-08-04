from django.shortcuts import render,redirect
from django . http import HttpResponse
from .models import Department,Doctor,Contact,Doctor1
from . forms import BookingForm
def appointment(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
        
    form=BookingForm()
    return render (request,'appointment.html',{'form':form})


        




def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=BookingForm()
    context ={
        'department':department,
        'doctor':doctor,
        'form':form,
        'doctor':doctor,
        

        
        
        
        
    }
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            return render(request,'index.html',context)
    
    return render(request,"index.html",context)
def about(request):
    doctor=Doctor.objects.all()
    return render (request,'about.html',{'doctor':doctor})
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        Phone=request.POST.get("Phone")
        message=request.POST.get("message")
        instance=Contact(name=name,email=email,Phone=Phone,message=message)
        instance.save()
        return redirect ('contact')



    return render (request,'contact.html',)


def departments(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            #return render(request,'index.html',{'form':form})
    form=BookingForm()
    return render (request,'departments.html',{'form':form})





    return render (request,'service.html')
def cardiology(request):
    cardiologist=Doctor1.objects.filter(speciality='Cardiology')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            
    form=BookingForm()
    return render (request,'cardiology.html',{'form':form,'doctors':cardiologist})
def EmergencyMedicine(request):
    EmergencyDepartment=Doctor1.objects.filter(speciality='Emergency Medicine')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            
    form=BookingForm()
    return render (request,'EmergencyMedicine.html',{'form':form,'doctors':EmergencyDepartment})

    
def Pathology(request):
    Pathologist=Doctor1.objects.filter(speciality='Pathology')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
    form=BookingForm()        
    return render (request,'Pathology.html',{'form':form,'doctors':Pathologist})
    
def Gastroenterology(request):
    Gastroenterologist=Doctor1.objects.filter(speciality='Gastroenterology')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
    form=BookingForm()        
    return render (request,'Gastroenterology.html',{'form':form,'doctors':Gastroenterologist})
    
def Radiology(request):
    Radiologist=Doctor1.objects.filter(speciality='Radiology')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
    form=BookingForm()        
    return render (request,'Radiology.html',{'form':form,'doctors':Radiologist})
    
def Obstetricsandgynaecology(request):
    Gynaecologist=Doctor1.objects.filter(speciality='Obstetrics and gynaecology')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
    form=BookingForm()        
    return render (request,'Obstetricsandgynaecology.html',{'form':form,'doctors':Gynaecologist})
    
def team(request):
    doctor=Doctor.objects.all()
    return render(request,'team.html',{'doctor':doctor})
def Forms(request):
    return render(request,'forms.html')

def Pediatrics(request):
    Pediatrics=Doctor1.objects.filter(speciality='Pediatrics')
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            form=BookingForm()
    form=BookingForm()        
    return render (request,'Pediatrics.html',{'form':form,'doctors':Pediatrics})






