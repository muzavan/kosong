from django.shortcuts import render
from level.forms import NewLevelForm
from django.shortcuts import render
# Create your views here.

def newLevel(request):
	if(request.method == "GET"):
		form = NewLevelForm()
		return render(request,"admin/newLevel.html",{"form" : form})
