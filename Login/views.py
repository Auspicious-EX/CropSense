from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def loginuser(request):
    return render(request,'authentication/login.html')
