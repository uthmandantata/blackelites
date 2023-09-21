from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    context = {}
    return render(request, "index.html", context)
def blog(request):
    context = {}
    return render(request, "blog.html", context)
def about(request):
    context = {}
    return render(request, "blog.html", context)
def umar_naveed(request):
    context = {}
    return render(request, "umar_naveed.html", context)
def contact(request):
    context = {}
    return render(request, "contact.html", context)
def services(request):
    context = {}
    return render(request, "services.html", context)
def team(request):
    context = {}
    return render(request, "team.html", context)