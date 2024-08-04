from django.contrib import admin
from .models import Department,Doctor,Booking,Contact,Doctor1

admin.site.register(Department)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('doc_name','doc_dep')
admin.site.register(Doctor,DoctorAdmin)
class BookingAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','doctor','booked','time','desc')
admin.site.register(Booking,BookingAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','Phone')
admin.site.register(Contact,ContactAdmin)
class Doctor1Admin(admin.ModelAdmin):
    list_display=('name','speciality')
admin.site.register(Doctor1,Doctor1Admin)






