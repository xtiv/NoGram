"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view"""
    
    template_name = 'users/detail.html'
    # Un slug es una forma de llamar a un campo de texto unico, en este caso el username
    slug_field = 'username'
    # slug_url_kwarg es como le llamaremos al endpoint
    slug_url_kwarg = 'username'
    # queryset es apartir de que conjunto de datos va a traer los datos
    queryset= User.objects.all()
    # Definimos el nombre de nuestro objeto que se traiga en el template
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        
        ##Traemos el contexto
        context = super().get_context_data(**kwargs)
        ## Obtenemos el objeto
        user = self.get_object()
        ## En la llave post filtramos solo aquellos posts que sean del usuario
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
    

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
    


# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data

#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()
            
#             ## Para este formate con kawrgs se debe crear la url con reverse
#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)

#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )



# def login_view(request):
#     """Login view."""
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username and password'})

#     return render(request, 'users/login.html')


# def signup(request):
#     """Sign up view."""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )

class SignupView(FormView):
    """Users sign up view"""
    
    template_name='users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view"""
    
    redirect_authenticated_user = True
    template_name = 'users/login.html'

# @login_required
# def logout_view(request):
#     """Logout a user."""
#     logout(request)
#     return redirect('posts:feed')

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""
    
    template_name = 'users/login.html'
    