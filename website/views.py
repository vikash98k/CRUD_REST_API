from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
 
def add_show(request):
	if request.method=='POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			nm=fm.cleaned_data['name']
			em=fm.cleaned_data['email']
			pw=fm.cleaned_data['password']
			reg=User(name=nm,email=em,password=pw)
			reg.save()	
			fm=StudentRegistration()
	else:
		fm = StudentRegistration()
	stud=User.objects.all()
	return render(request,'website/add_and_show.html',{'form':fm,'stu':stud})



def update_data(request,id):
	if request.method=="POST":
		pi = User.objects.get(pk=id)
		fm = StudentRegistration(request.POST,instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		pi = User.objects.get(pk=id)
		fm=StudentRegistration(instance=pi)
	return render(request,'website/update_student.html',{"form":fm})

def delete_data(request,id):
	if request.method=="POST":
		pi=User.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')


