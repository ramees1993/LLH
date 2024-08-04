from django import forms
from .models import Booking
from django.forms import TextInput,Select,Textarea


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['name','email','phone','doctor','booked','time','desc']
        widgets={ 
            'name': TextInput(attrs={
                'type':"text", 
                'class=':"form-control border-0" ,
                'placeholder':"Your Name",
                  'style':"height: 55px;,",
                  'style':"width: 250px;," 

            }),
            'email': TextInput(attrs={
                'type':"email", 
                'class=':"form-control border-0" ,
                'placeholder':"Your Email",
                  'style':"height: 55px;",
                  'style':"width: 250px;," 

            }),
            'phone': TextInput(attrs={
                'type':"phone", 
                'class=':"form-control border-0" ,
                'placeholder':"Your Phone",
                  'style':"height: 55px;",
                  'style':"width: 250px;,"  

            }),
            'doctor': Select(attrs={
                'class=':"form-control border-0" ,
                  'style':"height: 55px;" ,
                  'style':"width: 250px;,",
                  'style':"color: blue;"
                   

            }),
            'booked': TextInput(attrs={
                'type':"date", 
                'class=':"form-control border-0" ,
                  'style':"height: 55px;",
                  'style':"width: 250px;,"  

            }),
            'time': TextInput(attrs={
                'type':"time", 
                'class=':"form-control border-0" ,
                  'style':"height: 55px;" ,
                  'style':"width: 250px;," 
                   

            }),
            'desc': Textarea(attrs={
                'type':"textarea", 
                'class=':"form-control border-0" ,
                'placeholder':"Describe your problem",
                  'rows':"5" 

            })


        }