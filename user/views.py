from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def userRegister(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():

            # email işlemleri
            email = form.cleaned_data['email']
            subject = "Başarılı Kayıt"
            message = "Aramıza hoşgeldiniz!!!"

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )

            form.save()

            messages.success(request, "Kayıt başarılı!")
            return redirect('index')

    context = {
        'form':form
    }

    return render(request, "register.html", context)



def userLogin(request):

    if request.method == "POST":
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş başarılı!")
            return redirect('index')
        else:
            messages.error(request, "Kulanıcı adı ya da şifre hatalı!")
            return redirect('userlogin')


    return render(request, "login.html")


def userLogout(request):
    logout(request)
    messages.success(request, "Oturum kapatıldı!")

    return redirect('index')


def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Şifreniz başarıyla değiştirildi!")
            return redirect("userlogin")
        
        else:
            messages.error(request, "Bilgileriniz yanlış!")

    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form':form
    }

    return render(request, "password_change.html", context)


def accountDelete(request):

    user = request.user
    
    if request.method == "POST":
        if user.is_authenticated:
            user = request.user
            user.delete()
            logout(request)
            messages.success(request, "Hesabınız başarıyla silindi!Tebrikler!")
            return redirect('index')
        else:
            messages.error(request, "Hesabı silebilmek için giriş yapmalısın!")
            return redirect('login')

    return render(request, 'account_delete.html')