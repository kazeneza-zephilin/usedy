from django import forms

from .models import Item

INPUT_CLASSES = 'w-full p-3 border rounded-xl'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Item name',
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item description',
                'class': INPUT_CLASSES,
                'rows': 5
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Item price',
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

