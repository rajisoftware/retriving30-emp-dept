from django.shortcuts import render

# Create your views here.
from app.models import *
def display_DEPT(request):
    LOD=Dept.objects.all()
    d={'dept':LOD}
    return render(request,'display_dept.html',d)
def display_emp(request):
    LOE=Emp.objects.all()
    d={'emp':LOE}
    return render(request,'display_emp.html',d)
