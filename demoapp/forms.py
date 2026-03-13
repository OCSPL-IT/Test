from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'city']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none',
                'placeholder': 'Enter email'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none',
                'placeholder': 'Enter city'
            }),
        }