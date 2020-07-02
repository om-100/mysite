from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def profile(request, username):
    data = {
        'ram' : 'ram prasad sapkota',
        'krishna' : 'krishna prasad sapkota'
    }
    full_name = data[username]
    a = print("my fullname is: {}".format(full_name))
    return HttpResponse(a)
