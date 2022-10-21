from django.shortcuts import render,HttpResponse
from .models import employee
from .forms import employee_form

# Create your views here.
def employee_views(request):
    if request.method=='POST':
        form=employee_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Registered succesfully")
        else:
            return HttpResponse("Failed to register")
    else:
        form=employee_form()
        return render(request,'register.html',{'form':form})