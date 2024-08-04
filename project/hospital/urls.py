from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('cardiology/',views.cardiology,name="cardiology"),
    path('EmergencyMedicine/',views.EmergencyMedicine,name="EmergencyMedicine"),
    path('Pathology/',views.Pathology,name="Pathology"),
    path('Gastroenterology/',views.Gastroenterology,name="Gastroenterology"),
    path('Radiology/',views.Radiology,name="Radiology"),
    path('Obstetricsandgynaecology/',views.Obstetricsandgynaecology,name="Obstetricsandgynaecology"),
    path('team/',views.team,name="team"),
    path('appointment/',views.appointment,name="appointment"),
    path('departments/',views.departments,name="departments"),
    path('Pediatrics/',views.Pediatrics,name="Pediatrics")
    



    



    
    

    








]
