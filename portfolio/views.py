from django.shortcuts import render

# Create your views here.


def portfolio_home(request):
    context = {}
    return render(request, 'index.html', context)