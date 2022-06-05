from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
k=list()
s = Serial.objects.all()
for i in s:
    k.append(i.code)
# Create your views here.
def home(response):
    k = Product.objects.all()
    return render(response, 'App1/home.html', {'k': k})


def order(response):
    form=Order()
    return render(response, 'App1/order.html', {})


def sign_in(response):
    if response.method == 'POST':
        form = SignIn(response.POST)
        if form.is_valid():
            f1 = form.cleaned_data['first_name']
            f2 = form.cleaned_data['last_name']
            f3 = form.cleaned_data['company']
            f4 = form.cleaned_data['email']
            f5 = form.cleaned_data['serial']
            f6=form.cleaned_data['new_password']
            if f5 in k:

                user = UserOn(first_name=f1,
                              last_name=f2,
                              company=f3,
                              email=f4,
                              serial=f5)
                user.password=f6
                user.save()
                # I need to add emailing functionality
                pass
            else:
                pass
    else:
        form = SignIn()

    return render(response, 'App1/sign_in.html', {'form': form})


def search(response, page=int):
    return render(response, 'App1/results.html', {})


def new_code(response):
    return render(response, 'App1/new_code.html', {})


def verify(response, id=int):
    return render(response, 'App1/validate.html', {})


def about(response):
    return render(response, 'App1/about.html', {})


def community(response):
    k = CommentsB.objects.all()
    return render(response, 'App1/community.html', {'k': k})
