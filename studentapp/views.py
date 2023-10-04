import os
from django.shortcuts import redirect, render
from .models import student


def home(request):
    return render(request,'register.html')

def add_details(request):
    if request.method == 'POST':
        first=request.POST['fname']
        last=request.POST['lname']
        age=request.POST['age']
     
        gender=request.POST['gender']  
        qualification=request.POST['qualification']   
        image=request.FILES.get('file')
        stud=student(student_fname=first,student_lname=last,age=age,gender=gender,qualification=qualification,image=image)
        print("Save data...")
        stud.save()
        return redirect('show_details')
    
def show_details(request):
    stds=student.objects.all()
    return render(request,'showdetails.html',{'stud':stds})

def updatepage(request,pk):
    std=student.objects.get(id=pk)
    return render(request,'update.html',{'stud':std})

def update_student_details(request,pk):
    if request.method=='POST':
        std=student.objects.get(id=pk)
        std.student_fname=request.POST.get('fname')
        std.student_lname=request.POST.get('lname')
        std.age=request.POST.get('age')
      
        std.gender=request.POST.get('gender')
        std.qualification=request.POST.get('qualification')

        old=std.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            std.image=old
        else:
            std.image=new

        
        std.save()
        return redirect('show_details')
    return render(request,'update.html')

def deletepage(request,pk):
    studetail=student.objects.get(id=pk)
    studetail.delete()
    return redirect('show_details')



# Create your views here.
