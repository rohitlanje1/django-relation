from django.shortcuts import render,redirect
from .forms import CourseForm ,StudentForm
from .models import  Course ,Student
# Create your views here.

def add_course_view(request):
    form=CourseForm()
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_course_url")
    return render(request,"APP1/add_course.html",{"form":form})

def show_course_view(request):
    data=Course.objects.all()
    return render(request,"APP1/show_course.html",{"data":data})

def update_course_view(request,pk):
    data=Course.objects.get(cid=pk)
    form=CourseForm(instance=data)
    if request.method=="POST":
        form=CourseForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("show_course_url")
    return render(request,"APP1/add_course.html",{"form":form})


def delete_course_view(request,pk):
    data = Course.objects.get(cid=pk)
    if request.method=="POST":
        data.delete()
        return  redirect("show_course_url")
    return  render (request,"APP1/delete_course.html",{"data":data})


#####-------------------------------


def add_stud_view(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_stud_url")
    return render(request,"APP1/add_stud.html",{"form":form})

def show_stud_view(request):
    data=Student.objects.all()
    return render(request,"APP1/show_stud.html",{"data":data})

def update_stud_view(request,pk):
    data=Student.objects.get(sid=pk)
    form=StudentForm(instance=data)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("show_stud_url")
    return render(request,"APP1/add_stud.html",{"form":form})

def delete_stud_view(request,pk):
    data = Student.objects.get(sid=pk)
    if request.method=="POST":
        data.delete()
        return  redirect("show_stud_url")
    return  render (request,"APP1/delete_stud.html",{"data":data})

