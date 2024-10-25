from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def disp(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})

def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_pho=req.POST['pho']
        data=student.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,pho=std_pho)
        data.save()
        return redirect(disp)
    else:
        return redirect(disp)
    
def edit_std(req,id):
    data=student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll_no']
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_pho=req.POST['pho']
        student.objects.filter(pk=id).update(roll_no=roll,name=std_name,age=std_age,email=std_email,pho=std_pho)
        return redirect(disp)
    else:
        return render(req,'edit_std.html',{'data':data})
def delete_std(req,id):
    data=student.objects.get(pk=id)
    data.delete()
    return redirect(disp)


