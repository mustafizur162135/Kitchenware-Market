from django.shortcuts import *
from .myforms import *
from .dbmodels.userdao import *
from .dbmodels.user import *

# Create your views here.
def register(request):
    if request.method=="GET":
        django_form=RegisterForm()
        return render(request, 'registerpage.html', {'f':django_form})

    elif request.method=="POST":
        django_form=RegisterForm(request.POST)
        if django_form.is_valid():
            r_email=django_form.cleaned_data['email']
            r_pw=django_form.cleaned_data['pw']

            # print(r_email)
            # print(r_pw)

            userob=User(r_email, r_pw)
            userdao=UserDAO()
            try:
                userdao.insertUser(userob)
                django_form=RegisterForm()
                return render(request, 'registerpage.html', {'f':django_form, 'success':True})
            except:
                return render(request, 'registerpage.html', {'f':django_form, 'success':False})
        else:
            return render(request, 'registerpage.html', {'f':django_form})


def login(request):
    if request.method=="GET":
        django_form=LoginForm()
        return render(request, 'loginpage.html', {'f':django_form})

    elif request.method=="POST":
        django_form=LoginForm(request.POST)
        if django_form.is_valid():
            r_email=django_form.cleaned_data['email']
            r_pw=django_form.cleaned_data['pw']
            userob=User(r_email, r_pw)
            userdao=UserDAO()
            try:
                is_valid=userdao.authenticate_user(userob)
                if is_valid is True:
                    request.session['email']=r_email
                    return render(request, 'home.html')
                else:
                    return render(request, 'loginpage.html', {'f':django_form, 'isvalid':False})
            except:
                return render(request, 'loginpage.html', {'f':django_form, 'isvalid':False})

        else:
            return render(request, 'loginpage.html', {'f':django_form})

def home(request):
    if 'email' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('login')

def logout(request):
    del request.session['email']
    return redirect('login')
