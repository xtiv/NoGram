""" User views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exception
from django.db.utils import IntegrityError

# Form
from users.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
        
        
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


def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('passwd', True)
        passwordConfirmation = request.POST.get('passwd_confirmation', True)
        
        if password != passwordConfirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'Username is already in user'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        #Salvar objeto usuario
        user.save()
        
        profile = Profile(user=user)
        ## Siempre hay que salvar los objetos
        profile.save()
        
        return redirect('login')
        
    return render(request, 'users/signup.html')