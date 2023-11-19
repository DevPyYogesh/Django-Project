from django.shortcuts import redirect
from django.shortcuts import render
from .forms import SignupForm,feedback,contact
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def signout(request):
    return render(request,'signout.html')
def signup(request):
    return render(request,'signup.html')
def co(request):
    return render(request,'co.html')
# Create your views here.
def register(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/signin")
    else:
        fm = SignupForm()
    return render(request, "register.html", {'form':fm})

def signout(request):
    logout(request)
    return redirect("/signin")

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            #feed = FeedbackEntry()
            if user is not None:
                login(request, user)
                #return render(request, 'feedback.html',{'user': user, 'form': feed})
                return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request,"signin.html",{'form':fm})

def Gfeedback(request):
    if request.method == "POST":
        f1 = feedback(request.POST)
        if f1.is_valid():
            f1.save()

    else:
        f1 = feedback()
    return render(request,'feedback.html',{'feed':f1})

def ccontact(request):
    if request.method == "POST":
        c = contact(request.POST)
        if c.is_valid():
            c.save()

    else:
        c = contact()
    return render(request,'contact.html',{'feed':c})

def python(request):
    return render(request,'python.html')
def java(request):
    return render(request,'java.html')
def aws(request):
    return render(request,'aws.html')
def devops(request):
    return render(request,'devops.html')
def testing(request):
    return render(request,'testing.html')
def salseforce(request):
    return render(request,'salseforce.html')
def mean(request):
    return render(request,'mean.html')
def mern(request):
    return render(request,'mern.html')










