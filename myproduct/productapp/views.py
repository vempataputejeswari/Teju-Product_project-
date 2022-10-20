from django.shortcuts import render

# Create your views here.

def load_html(request):
	return render (request,'My.html')

