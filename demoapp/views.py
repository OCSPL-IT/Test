from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()   # insert into SQLite
            return redirect('student_form')
    else:
        form = StudentForm()

    students = Student.objects.all().order_by('-id')  # fetch from SQLite

    return render(request, 'student_form.html', {
        'form': form,
        'students': students
    })