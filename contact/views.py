from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import FormContactForm

def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'contactform.html', context)
