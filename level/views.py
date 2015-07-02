from django.shortcuts import render
from django.conf import settings
from level.forms import NewLevelForm
from level import models as util
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import datetime
# Create your views here.

def newLevel(request):
	if(request.method == "GET"):
		form = NewLevelForm()
		return render(request,"level/new-level.html",{"form" : form})

	elif(request.method == "POST"):
		form = NewLevelForm(request.POST,request.FILES)
		# check whether it's valid:
		if form.is_valid():
			image = uploadingFile(form.cleaned_data['image'])
			answer = form.cleaned_data['answer']
			hint = form.cleaned_data['hint']
			name = form.cleaned_data['name']
			linkProfile = form.cleaned_data['linkProfile']
			util.newLevel(image,answer,hint,name,linkProfile)
			return render(request,"level/thanks.html")
	else :
		return HttpResponse("Request is not identified");


def uploadingFile(f):
	name = 'level/'+str(datetime.datetime.now().time())+"_.png"
	media = settings.MEDIA_ROOT
	with open(media+"/"+name, 'wb+') as destination:
        	for chunk in f.chunks():
            		destination.write(chunk)

        	destination.close()
        	return name
