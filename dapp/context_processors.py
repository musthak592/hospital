from .models import department

def menu_links(request):
    links=department.objects.all()
    return dict(links=links)
