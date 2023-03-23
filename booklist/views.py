# from contextlib import redirect_stderr
# from msilib.sequence import InstallExecuteSequence
# from typing_extensions import Self
from urllib import request
from django.shortcuts import redirect, render
from booklist.forms import  BookModelForm, LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from booklist.models import books,Books
from django.views.generic import View
from django.contrib import messages

class BookView(View):
     def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book-add.html",{"form":form})
     def post(self,request,*args, **kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
         form.save()
         messages.success(request,"book added successfully")
       


        #  b_name=form.cleaned_data.get("bname")
        #  a_name=form.cleaned_data.get("aname")
        #  price=form.cleaned_data.get("price")
        #  Books.objects.create(bname=b_name,aname=a_name,price=price)
         return redirect("book-list")
        else:
            messages.error((request,"book creation failed"))

            # print(form.cleaned_data)
      #       books.append(form.cleaned_data)
      #       print(books)
      #   return render(request,"add_book.html",{"form":form})
class Booklistview(View):
    def get(self,request,*args, **kwargs):
         qs=Books.objects.all()
         return render(request,"book-list.html",{"books":qs})

class BookDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")

        qd=Books.objects.filter(id=id)
        # todo=[ todo for todo in todos if todo.get("id")==id].pop()

        return render(request,"book-detail.html",{"book":qd})

class BookDeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.filter(id=id).delete()
        messages.success(request,"book deleted successfully")

        # todo=[ todo for todo in todos if todo.get("id")==id].pop()
        # todos.remove(todo)
        return redirect("book-list")


class BookEditview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        # todo=[ todo for todo in todos if todo.get("id")==id].pop()
        qs=Books.objects.get(id=id)
        form=BookModelForm(instance=qs)
        return render(request,"book-update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request,"edit successfully")
        else:
             messages.error(request,"edit failed")

    #    id=kwargs.get("id")
    #    Books.objects.filter(id=id).update(**form.cleaned_data)
        return redirect("book-list")


class RegistrationView(View):
    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data) 
            messages.success(request,"registration completed succesfully")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"registration.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if User:
                login(request,user)
                return redirect("book-list")
            else:
                print("login failed")
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})


def Signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")





   





       
       





    
    

