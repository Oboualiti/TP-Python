from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        
        # Vérification des identifiants dans la base de données
        user = authenticate(username=u, password=p) 
        
        if user is not None:
            auth_login(request, user) 
            return redirect('/') 
        else:
            messages.info(request, 'Identifiants invalides') 
            return redirect('login')
            
    return render(request, 'login.html') 


def counter(request):
    if request.method == 'POST':
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    return render(request, 'counter.html')

def register(request):
    if request.method == 'POST':
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['password']
        p2 = request.POST['password2']
        
        if p1 == p2:
            if User.objects.filter(username=u).exists():
                messages.info(request, 'Le nom d\'utilisateur existe déjà')
                return redirect('register')
            else:
                user = User.objects.create_user(username=u, email=e, password=p1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Mots de passe non identiques')
            return redirect('register')
    return render(request, 'register.html')