# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    
    ## Modificar las vistas
    list_display = ('pk','user','phone_number','website', 'picture')
    
    ## Linkear fields para ir a los detalles
    list_display_links = ('pk','user')
    
    ## Editar campos sin ir a detalles
    list_editable = ('website', 'phone_number', 'picture')
    
    ## Crear campos de busqueda
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'phone_number'
    )
    
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    ## Las comas en las tuplas se deben tener presente, cuando es solo una parte
    fieldsets = (
        ('Profile', {
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(('website','phone_number'),('biography'))
        }),
        ('Metadata',{
            'fields':(('created','modified'),)
        })
    )
    
    ## created y modified son datos que no se pueden modificar se deben especificar en la propiedad "readonly_fields"
    
    readonly_fields = ('created','modified')
    

class ProfileInline(admin.StackedInline):
    
    model = Profile
    can_delete = False
    varbose_name_plural ='profiles'
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

## No se registran con decordador, se deregistra el que existia y registrar el nuevo que se edito

admin.site.unregister(User)
# Puede recibir el modelos y la clase de admin, que va usar
admin.site.register(User,UserAdmin)