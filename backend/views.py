from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from backend.models import Lead,contact,Idcard

# Create your views here.
def viewlogin(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                messages.success(req, "Login Successfully")
                return redirect(indexpage)
            else:
                messages.error(req, "Invalid User")
        return redirect(viewlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(viewlogin)
def indexpage(request):
    return render(request,"home.html")
def viewlead(request):
    data = Lead.objects.all()
    return render(request,"view_lead.html",{'data':data})
def deletelead(request,dataid):
    data=Lead.objects.filter(id=dataid)
    data.delete()
    return redirect(viewlead)
def messageview(request):
    data = contact.objects.all()
    return render(request,"message_view.html",{'data':data})
def deletemessage(request,dataid):
    data=contact.objects.filter(id=dataid)
    data.delete()
    return redirect(viewlead)
def viewid(request):
    data = Idcard.objects.all()
    return render(request,"view_id.html",{'data':data})
def deleteid(request,dataid):
    data=Idcard.objects.filter(id=dataid)
    data.delete()
    return redirect(viewid)

