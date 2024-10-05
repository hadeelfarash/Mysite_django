# forms.py
from django import forms
from .models import Contractor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'id_number', 'mobile_number', 'profession', 'notes']



class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['subscriber_name', 'id_number', 'phone_number', 'request_number', 'residence', 'notes']
      


from .models import Objection,Note

class ObjectionForm(forms.ModelForm):
    class Meta:
        model = Objection
        fields = ['note', 'image']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note', 'image']
        
        


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'id_number', 'mobile_number', 'profession','salary' ,'notes']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_code', 'description']  # الحقول التي سيتم عرضها في النموذج
        
        


class CompanyorderForm(forms.ModelForm):
    class Meta:
        model = Companyorder
        fields = ['item_code', 'price', 'quantity'] 