from django.shortcuts import render

def index(request):
    context= {

    }
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')