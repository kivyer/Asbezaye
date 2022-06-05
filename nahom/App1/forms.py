from django import forms


class SignIn(forms.Form):
    first_name = forms.CharField(label='Your first name:', min_length=3, max_length=100)
    last_name = forms.CharField(min_length=3, max_length=60, label='your last name:')
    company = forms.CharField(max_length=80, required=False)
    email = forms.EmailField(max_length=60, label='Email')
    new_password = forms.PasswordInput()

    serial = forms.CharField(max_length=10, label='Activation code')
class Order(forms.Form):
    user=forms.CharField(max_length=100,label='your user name')
    email=forms.EmailField(label='your Email:')
    product=forms.SelectMultiple