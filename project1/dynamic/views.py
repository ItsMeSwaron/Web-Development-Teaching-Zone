from django.shortcuts import render

# Create your views here.

def printer(request):
    return render(request, 'dynamic_view.html')