""" User views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

def login_view(request):
    """Login view"""
    
    if request.method == 'POST':
        print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            ## Redireccionamos al feed
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalidad username or password'})
    return render(request, 'users/login.html')  


# Que solo permita con sesion iniciada
@login_required
def logout_view(request):
    """LogOut view"""
    
    logout(request)
    return redirect('login')