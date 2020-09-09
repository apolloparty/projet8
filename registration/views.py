from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

def register2(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Compte crée pour " + user)
            return redirect(myaccount2)
    context = {'form': form}
    return render(request, 'register2.html', context)

def register(request):
    """
    """
    user_list = ["", "", "", ""]

    if 'btn_dis' in request.POST:
        print(request.POST.get('btn_dis'))
        messages.success(request, "Déconnecté")
        return redirect(register)
    if request.method == 'POST':
        user_list[0] = request.POST['username']
        user_list[1] = request.POST['email']
        user_list[2] = request.POST['password']
        user_list[3] = request.POST['password-conf']
        try:
            temp = User.objects.filter(username=user_list[0]).values('username')
            user_confirm = temp[0]['username']
            if user_list[0] == user_confirm:
                messages.error(request, "Le pseudonyme existe déjà")
                return redirect(register)
        except:
            pass
        try:
            temp = User.objects.filter(email=user_list[1]).values('email')
            email_confirm = temp[0]['email']
            print(user_list[1], email_confirm)
            if user_list[1] == email_confirm:
                messages.error(request, "L'email est déjà utilisé")
                return redirect(register)
        except:
            pass
        if user_list[2] != user_list[3]:
            messages.error(request, "Mauvais mot de passe de confirmation")
            return redirect(register)

        table_user = User(\
            username = user_list[0],\
            email = user_list[1],
            password = user_list[3]
            )
        table_user.save()
        return redirect(myaccount2)
    return render(request, 'register.html')

def myaccount(request):
    """
    """
    user_list = ["", ""]
    if 'username' in request.POST:
        user_list[0] = request.POST['username']
    if 'password' in request.POST:
        user_list[1] = request.POST['password']
        print(user_list)
        try:
            temp = User.objects.filter(username=user_list[0]).values('username', 'id', 'password')
            user_confirm = temp[0]['username']
            print(user_confirm)
            if user_list[0] == user_confirm:
                print("utilisateur existant")
            password_confirm = temp[0]['password']
            if user_list[1] == password_confirm:
                print("Bon mot de passe")
            else:
                messages.error(request, "Mauvais mot de passe")
                return redirect(myaccount)
        except:
            messages.error(request, "Utilisateur inexistant")
            return redirect(myaccount)
        messages.success(request, "Connecté")

    return render(request, 'myaccount.html')

#@unauthenticated_user
def myaccount2(request):
    """
    """
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenue " + username)
            return redirect(myaccount2)
        else:
            messages.error(request, "Utilisateur inexistant ou mauvais mot de passe")
            return redirect(myaccount2)
    context = {}

    return render(request, 'myaccount2.html', context)

def disconect(request):
    if "btn_dis" in request.POST:
        logout(request)
        messages.success(request, "Déconnecté")
    else:
        redirect('home')
    return redirect(myaccount2)

@login_required(login_url='myaccount2')
def client(request):
    user_name = request.user.username # get the username of the user, use id if necessary
    email = request.user.email
    context = {
        "username": user_name,
        "email": email,
    }
    return render(request, 'client.html', context)