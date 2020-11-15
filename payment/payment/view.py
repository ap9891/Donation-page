from django.http import HttpResponse
from django.shortcuts import  render

def donate(request):
    return render(request,'donate.html')
def whydonte(request):
    return render(request,'whydonte.html')
def thought(request):
    return render(request,'thought.html')
def surprise(request):
    return render(request,'surprise.html')