from django import forms
#import datetime
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Prof,Vehicle,Ride
class DriverRegistrationForm(forms.Form):
    FOUR = 4
    SIX = 6
    CAP_CHOICES = (
        (FOUR, 4),
        (SIX,6),
    )
    SEDAN = "SEDAN"
    MINIVAN = "MINI"
    CROSSOVER = "CROSS"
    CAR_CHOICES = (
        (SEDAN, 'Sedan'),
        (MINIVAN, 'Minivan'),
        (CROSSOVER, 'Crossover'),
    )
    PlateNumber= forms.CharField(label='License Plate Number', max_length=8)
    Capacity = forms.ChoiceField(widget = forms.Select, choices = CAP_CHOICES)
    Type = forms.ChoiceField(widget = forms.Select, choices = CAR_CHOICES)
    

#added here
class DriverUpdateForm(forms.Form):
    FOUR = 4
    SIX = 6
    CAP_CHOICES = (
        (FOUR, 4),
        (SIX,6),
    )
    SEDAN = "SEDAN"
    MINIVAN = "MINI"
    CROSSOVER = "CROSS"
    CAR_CHOICES = (
        (SEDAN, 'Sedan'),
        (MINIVAN, 'Minivan'),
        (CROSSOVER, 'Crossover'),
    )
    PlateNumber= forms.CharField(label='License Plate Number', max_length=8)
    Capacity = forms.ChoiceField(widget = forms.Select, choices = CAP_CHOICES)
    Type = forms.ChoiceField(widget = forms.Select, choices = CAR_CHOICES)
    isDriver = forms.BooleanField(label='Still want to be a driver',required=False,initial=True)

    
class RideRequestForm(forms.Form):
    SEDAN = "SEDAN"
    MINIVAN = "MINI"
    CROSSOVER = "CROSS"
    EMPTY = ""
    CAR_CHOICES = (
        (EMPTY, ''),
        (SEDAN, 'Sedan'),
        (MINIVAN, 'Minivan'),
        (CROSSOVER, 'Crossover'),
    )
    #pickUpTime =  forms.DateField(initial=datetime.date.today)
    pickUpTime =  forms.DateTimeField(initial=datetime.now())
    canBeShared = forms.BooleanField(label = 'Share', initial = False, required = False) #default false
    num_pass = forms.IntegerField(label = 'Number of Passengers in your party',
                                  initial = 1, min_value = 1, max_value = 6) #up to 6?
    vehicle_type = forms.ChoiceField(widget = forms.Select, choices = CAR_CHOICES, required = False)
    destination = forms.CharField(label='Destination',max_length=100)

class JoinRequestForm(forms.Form):
    num_pass = forms.IntegerField(label = 'Number of Passengers in your party',
                                  initial = 1, min_value = 1, max_value = 6) #up to 6?

    

#new add, for user register with email
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
'''
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
'''
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Enter email',required=True)
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

import pdb
class EditProfForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean_username(self):
        pdb.set_trace()
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username = username).count() >= 1:
            raise  ValidationError("Please enter a new username (this is a duplicate)")
        return username
 
    def clean_email(self):
        pdb.set_trace()
        email = self.cleaned_data['email'].lower()
        return email
    
    def clean_password2(self):
        pdb.set_trace()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2
 
    def save(self, pk, commit=True):
        pdb.set_trace()
        user = User.objects.filter(pk=pk).first()
        user.username=self.cleaned_data['username'],
        user.email=self.cleaned_data['email'],
        user.password=self.cleaned_data['password1']
        return user
    

