from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def djform(request):
    SUFO=SignUp()
    d={'SUFO':SUFO}
    if request.method=='POST':
        
        return HttpResponse('data submited')
    return render(request,'djform.html',d)