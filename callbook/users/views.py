from django.shortcuts import render, get_object_or_404
from .models import Person


def userspage(request):
    return render(request, 'users.html')


def get_user(request, pk):
    if pk == 88:
        return render(request, 'flag.html', {'flag': 'kvvu{test_flag}'})
    user = Person.objects.get(id=pk)
    if user:
        return render(request, 'userpage.html', {'user': user})
    else:
        return render(request, 'user404.html')
