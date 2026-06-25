from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST 
        fname = data.get('fname')
        lname = data.get('lname')
        uname = data.get('uname')
        password = data.get('password') 

        if User.objects.filter(username=uname).exists():
            return render(request,"index.html",{"error":"invalid input"})
        u = User(first_name=fname,last_name=lname,username=uname,password=password)
        u.set_password(password)
        u.save()
        return render(request,"index.html",{"msg":"Registrationdone"})
    return render(request,"index.html")

