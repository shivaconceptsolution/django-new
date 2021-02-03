from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,"employee/welcome.html")


def tutorials(request):
	return render(request,"employee/tutorials.html")



def operation(request):
	return render(request,"employee/operation.html")


def opecode(request):
	a = request.POST['txtnum1']
	b = request.POST['txtnum2']
	if request.POST.get("btnadd"):
		c=int(a)+int(b)
	elif request.POST.get("btnsub"):
		c=int(a)-int(b)
	elif request.POST.get("btnmult"):
		c=int(a)*int(b)
	elif request.POST.get("btndiv"):
		c=int(a)/int(b)				
	return render(request,"employee/operation.html",{'key':'result is '+str(c),'a':a,'b':b})			
