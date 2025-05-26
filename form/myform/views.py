from django.shortcuts import render
from .models import Userdata

def index(request):
    if request.method == 'POST':
        data = Userdata(
            fname = request.POST.get('firstName'),
            lname = request.POST.get('lastName'),
            email = request.POST.get('userEmail'),
            review = request.POST.get('textArea'),
        )
        data.save()
        return render(request,"Thankyou.html")
    return render(request, 'index.html')

def thankyou(request):
    return render(request,'Thankyou.html')
        
        
    
