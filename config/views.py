# Create your views here.
from django.http import JsonResponse

# auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def index(request):
    return JsonResponse({'message': 'Hello, world!'})


#jwt login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'login success'})
        else:
            return JsonResponse({'message': 'login fail'})
    else:
        return JsonResponse({'message': 'login fail'})

