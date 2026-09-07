from django.shortcuts import render

# Create your views here.
def app2v1(request):
    return render(request, 'app2v1.html')

def app2v2(request):
    return render(request, 'app2v2.html')