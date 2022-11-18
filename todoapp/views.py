from django.shortcuts import render


def index(request):
    # if request.user.is_authenticated:
    #     user_name = user.username
    # else:
    
    return render(request, 'todoapp/index.html', {})
