from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)

def timeline(request):
    context = {}
    return render(request, 'timeline.html', context)

def blog(request):
    context = {}
    return render(request, 'blog-list.html', context)

def blogdetail(request):
    context = {}
    return render(request, 'blog-detail.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)