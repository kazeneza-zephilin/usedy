from django.shortcuts import render
from item.models import Catergory, Item

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Catergory.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')