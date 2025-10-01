from django.shortcuts import redirect, render, get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import EditItemForm, NewItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[:4]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            return redirect('item:detail', pk=new_item.pk)
    else:
        form = NewItemForm()
    return render(request, 'item/new.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/edit.html', {
        'form': form,
        'item': item,
        'title': 'Edit Item'
    })



@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')
