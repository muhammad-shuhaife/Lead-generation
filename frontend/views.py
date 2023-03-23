from django.shortcuts import render,redirect
from backend.models import Lead,contact,Idcard,Candidate
from django.contrib import messages

# Create your views here.
def loginfront(request):
    return render(request,"loginf.html")
def loginfrontf(request):
    if request.method=='POST':
        username_r=request.POST.get("usernamel")
        password_r = request.POST.get("passwordl")
        if Lead.objects.filter(Name=username_r,Password=password_r).exists():
            request.session['usernamel']=username_r
            request.session['passwordl'] = password_r
            messages.success(request,"Login Successfully")
            return redirect(fhomepage)
        else:
            messages.error(request, "Invalid User")
            return render(request,'loginf.html',{'msg':"sorry...invalid username or password"})
def logoutfront(request):
    del request.session['usernamel']
    del request.session['passwordl']
    messages.success(request, "Logged Out Successfully")
    return redirect(loginfront)
def saveregistration(req):
    if req.method== "POST":
        NAME=req.POST.get('username')
        EMAIL=req.POST.get('email')
        MOBILE=req.POST.get('mobile')
        SOURCE = req.POST.get('source')
        PASSWORD = req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('confirmpassword')
        obj=Lead(Name=NAME,Email=EMAIL,Mobile=MOBILE,Source=SOURCE,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD)
        obj.save()
        messages.success(req,"Registered Successfully")
        return redirect(loginfront)

def fhomepage(request):
    return render(request, "homef.html",)
def savecontact(req):
    if req.method== 'POST':
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        SUBJECT=req.POST.get('subject')
        MESSAGE=req.POST.get('message')
        obj=contact(Name=NAME,Email=EMAIL,Subject=SUBJECT,Message=MESSAGE)
        obj.save()
        messages.success(req,"Sent Successfully")
        return redirect(fhomepage)

def id_card(request):
    return render(request, "id_card details.html",)
def save_card(req):
    if req.method== 'POST':
        NAME=req.POST.get('cname')
        NUMBER = req.POST.get('cnumber')
        CVV=req.POST.get('ccvv')
        DATE=req.POST.get('cdate')
        obj=Candidate(Name=NAME,Number=NUMBER,Cvv=CVV,Date=DATE)
        obj.save()
        messages.success(req,"Paid Successfully")
        return redirect(id_card)


def id_details_save(request):
    if request.method== 'POST':
        NAME = request.POST['name']
        EMAIL = request.POST['email']
        ADDRESS = request.POST['address']
        CITY = request.POST['city']
        MOBILE = request.POST['mobile']
        IDNUMBER = request.POST['randomNumber']
        IMAGE = request.FILES['image']
        SIGN = request.FILES['sign']
        obt: Idcard = Idcard(Image=IMAGE,Sign=SIGN,Name=NAME,Email=EMAIL,Address=ADDRESS,City=CITY,Mobile=MOBILE,Idnumber=IDNUMBER)
        obt.save()
        return redirect('idcard',obt.id)
    else:
        return render(request, "id_card details.html",)

def idcard(request, id):
    obt = Idcard.objects.get(id=id)
    context = {'image': obt.Image,'sign': obt.Sign,'randomNumber': obt.Idnumber,'mobile': obt.Mobile,
               'city': obt.City,'address': obt.Address,'email': obt.Email,'name': obt.Name}
    return render(request, 'id_card.html', context)


