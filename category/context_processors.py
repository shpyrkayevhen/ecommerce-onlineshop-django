# === TAKES REQUEST AND RETURN THE DICTIONARY DATA === #
#     CONNECT CONTEXT PROCESSORS IN settings.py 

from .models import Category

def menu_links(request):
    # === FETCH ALL CATEGORIES FROM DB === #
    links = Category.objects.all()
    return dict(links=links)