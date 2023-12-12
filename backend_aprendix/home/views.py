from django.shortcuts import render

# Create your views here.
def vista_about(request):
    return render(request, 'about.html')
