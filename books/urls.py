"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booklist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/add',views.BookView.as_view(),name="book-add"),
    path('books/list',views.Booklistview.as_view(),name="book-list"),
    path('books/detail/<int:id>',views.BookDetailView.as_view(),name="book-detail"),
    path('books/remove/<int:id>',views.BookDeleteview.as_view(),name="book-delete"),
    path('books/change/<int:id>',views.BookEditview.as_view(),name="book-edit"),
    path('register',views.RegistrationView.as_view(),name="register"),
    path('login',views.LoginView.as_view(),name="signin"),
    path('logout',views.Signout,name="signout"),








]
