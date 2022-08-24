from applications.home.models import Home

# procesor para recuperar teléfono y correo del registro home

def home_contac(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.email,
    }