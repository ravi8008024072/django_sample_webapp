from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     email_base, provider = email.split('@')
    #     domain, extension = provider.split('.')
    #     if not domain == 'raviit':
    #         raise forms.ValidationError("pls enter valid domain name like 'raviit' (Ex: abc@raviit.in)")
    #     if not extension == 'in':
    #         raise forms.ValidationError("pls make sure your extension ends with .in (EX: abc@raviit.in)")
    #     return email


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']


    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == 'raviit':
            raise forms.ValidationError("pls enter valid domain name like 'raviit' (Ex: abc@raviit.in)")
        if not extension == 'in':
            raise forms.ValidationError("pls make sure your extension ends with .in (EX: abc@raviit.in)")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        #write validation code here
        return full_name
