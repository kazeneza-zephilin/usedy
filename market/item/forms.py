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
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image', 'is_sold')
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
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded'
            })
        }

