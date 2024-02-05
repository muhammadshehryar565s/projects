from django.shortcuts import render
from .forms import imageForm
from .models import getimage

# Create your views here.

def getout(request):
    if request.method=='POST':
        form =imageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=imageForm
    img=getimage.objects.all()
    return render(request,'my_app/index.html', {'img':img , 'form':form})