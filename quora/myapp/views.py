from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
logged_in=0
def index_view(request):
    questions=questions_model.objects.all()
    return render(request,'home.html',{'questions':questions})

def question_detail_view(request,id):
    question=questions_model.objects.get(id=id)
    answers=question.answers.all()
    return render(request,'questionDetail.html',{'question':question,'answers':answers})
@login_required
def Ask_question(request):
    form=question_form()
    if request.method=='POST':
        qn=request.POST.get('question', None)
        user=User.objects.get(id=request.user.id)
        an=questions_model.objects.create(question=qn,author=user)
        an.save()
        return HttpResponseRedirect('/')
    return render(request,'ask.html',{'form':form})

def answer_view(request,id):


    form=answer_form()

    if request.method=='POST':
        ans=request.POST.get('answer', None)
        qu=questions_model.objects.get(id=id)
        a=answers_model.objects.create(answer=ans,question=qu)
        a.save()
        return HttpResponseRedirect('/')
    return render(request,'answer.html',{'form':form})
#  bio email college  profession
def user_profile(request,id):

    user=User.objects.get(id=id)
    bio=user.profile.bio
    bio=user.profile.bio
    email=user.profile.email
    college=user.profile.college
    profession=user.profile.profession
    return render(request,'profile.html',{'name':user.username,'bio':bio,'email':email,'college':college,'profession':profession})



def dbprint():

    te=User.objects.get(id=1)
    #print('dbprintaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(te.username,te.profile.bio)

def logout_redirect(request):
    return render(request,'logout_redirect_page.html')

def signup_view(request):
    form=signup_form()
    pform= profile_form()

    if request.method=='POST':
        uform=signup_form(request.POST)
        userr=uform.save()
        userr.set_password(userr.password)
        userr.save()
        #print(user.id,'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff____________________________')

        fbio=request.POST.get('bio', None)
        femail=request.POST.get('email', None)
        fcollege=request.POST.get('college', None)
        fproession=request.POST.get('profession', None)
        #bio email college  profession

        a=profile.objects.create(user=userr,bio=fbio,email=femail,college=fcollege,profession=fproession)


        return render(request,'logout_redirect_page.html')


    return render(request,'signup.html',{'form':form,'profile':pform})
