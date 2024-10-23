from django.shortcuts import render,redirect
from .models import *
std1=[]
# Create your views here.
def disp(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})

def add_std(req):
    return render(req,'add_std.html')

# def std_form(req):
#     if req.method=='POST':
#         id=req.POST['id']
#         Task=req.POST['Task']
#         std1.append({'id':id,'Task':Task})
#         print(std1)
#         return redirect(std1)
#     return render(req,"todo.html",{'todo':std1})