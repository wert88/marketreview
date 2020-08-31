from django.contrib.auth.models import User
from django import forms
from .models import ContactModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'email', 'password')

        def clean(self):
        	cleaned_data = super(UserForm, self).clean()
        	password = cleaned_data.get("password")
        	confirm_password = cleaned_data.get("confirm_password")

        	if password != confirm_password:
        	    raise forms.ValidationError("password and confirm_password does not match")
				
class ContactForm(forms.ModelForm):
	class Meta:
		model= ContactModel
		fields= ["from_email", "subject", "message"]
