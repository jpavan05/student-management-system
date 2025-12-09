from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        course = request.POST['course']
        Student.objects.create(name=name, email=email, age=age, course=course)
        return redirect('student_list')
    return render(request, 'students/students_form.html')

def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'students/students_form.html', {'student': student})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')
