"""Post views"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'My Dog.',
        'user': {
            'name': 'Steven Gonzalez',
            'picture': 'https://picsum.photos/id/1023/80/80'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/500/500'
    },
    {
        'title': 'Khe.',
        'user': {
            'name': 'Maria Bohorquez',
            'picture': 'https://picsum.photos/id/1027/80/80'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/84/500/500'
    },
    {
        'name': 'Natural web',
        'user': {
            'name':'Karen Prieto',
            'picture': 'https://picsum.photos/id/1027/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/784/500/500'
    },
    
]

@login_required
def list_post(request):
    """List existing posts"""
    #Primero el request, luego el template el otro argumento que recibe es un dict
    return render(request, "posts/feed.html", {'posts': posts})
