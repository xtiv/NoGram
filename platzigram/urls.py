""" Platzigram URLs module """

#Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Platzigram
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    # En el path se pone al final el "/"
    path("admin/", admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    
    path('posts/', posts_views.list_post)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

