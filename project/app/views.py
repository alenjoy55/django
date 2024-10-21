from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[]

# Create your views here.
def fun1(request):
    return HttpResponse("welcome")

def fun2(request):
    a={'name':'arun','age':19}
    return HttpResponse(a)

def fun3(request,a,b):
    return HttpResponse(a)

def fun4(request,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)
def index_page(request):
    name="alen"
    age="22"
    place="tsr"
    return render(request,'index.html',{'name':name,'age':age,'place':place})
def demo(req):
    # l=[1,2,3,4,5]
    # return render(req,'demo.html',{"data":l})
    # d={'name':'alen','age':20}
    # return render(req,'demo.html',{'data':d})
    l=[{'name':'alen','age':22},{'name':'deepak','age':20},{'name':'ibin','age':23}]
    d={'name':'alen','age':22}
    return render(req,"demo.html",{'data':l,'data1':d})

def second(req):
    return render(req,'second.html')

def todo1(req):
    if req.method=='POST':
        id=req.POST['id']
        Task=req.POST['Task']
        todo.append({'id':id,'Task':Task})
        print(todo)
        return redirect(todo1)
    return render(req,"todo.html",{'todo':todo})

