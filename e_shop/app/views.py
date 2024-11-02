from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    else:

        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname
                    return redirect(shop_home)
                else:
                    req.session['user']=uname
                    return redirect(user_home)
            else:
                messages.warning(req, "invaild uname or password")
            return redirect(shop_login)
        else:
            return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(shop_login)
        except:
                messages.warning(req, "user already exists")
                return redirect(register)

    else:
        return render(req,'register.html')

#------------- admin-------------------------------------------------------
    
def shop_home(req):
    if 'shop' in req.session:
        product=Product.objects.all()
        return render(req,'shop/shop_home.html',{'products':product})
    else:
        return render(shop_login)

def add_product(req):
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        file=req.FILES['img']
        data=Product.objects.create(product_id=id,name=name,price=price,offer_price=offer_price,img=file)
        data.save()
    return render(req,'shop/add_product.html')

def edit_product(req,id):
    Pro=Product.objects.get(pk=id)
    if req.method=='POST':
        e_id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        file=req.FILES.get('img')
        print(file)
        if file:
            Product.objects.filter(pk=id).update(product_id=e_id,name=name,price=price,offer_price=offer_price,img=file)
        else:
            Product.objects.filter(pk=id).update(product_id=e_id,name=name,price=price,offer_price=offer_price)
            return redirect(shop_home)
    return render(req,'shop/edit_product.html',{'data':Pro})

def delete_product(req,id):
    data=Product.objects.get(pk=id)
    url=data.img.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(shop_home)
#-----------------------user---------------------------
def user_home(req):
    if 'user' in req.session:
        product=Product.objects.all()
        return render(req,'user/user_home.html',{'products':product})
    
def view_product(req,id):
    log_user=User.objects.get(username=req.session['user'])
    product=Product.objects.get(pk=id)
    try:
        cart=Cart.objects.get(product=product,user=log_user)
    except:
        cart=None
    return render(req,'user/view_pro.html',{'product':product,'cart':cart})

def add_cart(req,pid):
    Products=Product.objects.get(pk=pid)
    print(Products)
    user=User.objects.get(username=req.session['user'])
    print(user)
    data=Cart.objects.create(user=user,product=Products)
    data.save()
    return redirect(cart_display)

def cart_display(req):
    log_user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=log_user)
    return render(req,'user/cart_display.html',{'data':data})

def cart_delete(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(cart_display)
    

