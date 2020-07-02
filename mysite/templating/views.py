from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def hello_template(request):
    template = loader.get_template('hello.html')
    context = {}
    template_data = template.render(context,request)
    return HttpResponse(template_data)

def hello_render(request):
    context = {
        'name' : 'om'
    }
    return render(request,'hello.html',context )


