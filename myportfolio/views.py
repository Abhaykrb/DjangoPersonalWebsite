from django.shortcuts import render,redirect
from .models import Projects,contact
from myportfolio.forms import contactForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
   #filtering done so that we get all items in required place only
   proGIS=Projects.objects.all().filter(topicc='GIS')                                                                  
   proRS=Projects.objects.all().filter(topicc='Remote_Sensing')                                                                  
   proWM=Projects.objects.all().filter(topicc='WebMapping')                                                                  
   return render(request, 'index.html', {'proGIS':proGIS,'proRS':proRS,'proWM':proWM})

def contact(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = contactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL:
            fn=form['firstname'].value()#to access the first name entered
            return render(request,'contact.html',{'message':fn})
    else:
        # GET, generate unbound (blank) form
        return redirect('/')
 