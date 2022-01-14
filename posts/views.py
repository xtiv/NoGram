"""Post views"""

# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Utilities
from datetime import datetime

# Models
from posts.models import Post

# Form
from posts.forms import PostForm

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    # Nombre del query en el template o sea en el contexto
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""
    
    template_name = 'posts/detail.html'
    queryset= Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new post"""
    
    template_name = 'posts/new.html'
    form_class = PostForm
    ## "reverse_lazy" lo que hace es evaluar la url hasta que la necesitemos
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
        

# @login_required
# def create_post(request):
#     """Create new post view"""
#     if request.method == 'POST':
#         ## Enviamos el formulario los datos del request, como hay una foto se envia tambien el .FILES
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect ('posts:feed')
#     else:
#         form = PostForm()
    
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )


