from django.shortcuts import render, get_object_or_404, redirect
from .models import Person


def userspage(request):
    if request.POST:
        sn = request.POST.get("sn")
        if Person.objects.filter(surname=sn):
            user = Person.objects.filter(surname=sn)[0]
            return redirect('/users/{}'.format(user.id))
        else:
            return render(request, 'user404.html')
    return render(request, 'users.html')


def get_user(request, pk):
    if pk == 88:
        return render(request, 'flag.html', {'flag': 'kvvu{test_flag}'})
    try:
        user = Person.objects.get(id=pk)
        return render(request, 'userpage.html', {'user': user})
    except:
        return render(request, 'user404.html')
    # if user:
    #     return render(request, 'userpage.html', {'user': user})
    # else:
    #     return render(request, 'user404.html')
