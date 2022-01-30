"""Platzigram middleware catalog"""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.
    
    Ensure every usser that is interactin with the platform have
    ther progfile picture and biography.
    """
    
    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response
        
    def __call__(self, request):
            """Code to be executed for each request before the view is called"""
            ## Aqui ponemos la lógica
            
            # "is_anonymous" es una propiedad que agrega el middleware
            
            # Nos aseguramos que el user este logeado
            
            # Esto porque si es anonimo posiblemente este en el log-in
            if not request.user.is_anonymous:

                if not request.user.is_staff:
                    profile = request.user.profile
                    # if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                    #     return redirect('users:update_profile')
                    ## Si no tiene "" o no tiene "" entonces:
                    if not profile.picture or not profile.biography:
                        ## Debemos sacar al cliente de la peticion o creara un bucle que causará error
                        ### Llamar urls por su name tag se hace con reverse (función de Django)
                        ### Que no este el cliente en update o logout porque si no se quedará en el bucle
                        if request.path not in [reverse('users:update'), reverse('users:logout')]:
                            return redirect('users:update')
            
            response = self.get_response(request)
            return response
