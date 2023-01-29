from django.shortcuts import render


def indexpage(request):
    return render(request, 'index.html')


def login(request):
    if request.POST:
        return render(request, 'login.html', {'help': 'Иногда мы ищем то, чего нет...'})
    return render(request, 'login.html', {'help': ''})
