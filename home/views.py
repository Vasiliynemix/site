from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'home/index.html', context)
