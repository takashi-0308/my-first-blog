from django.shortcuts import render

def index(request):
    return render(request, 'ishida_HP/index.html', {})
