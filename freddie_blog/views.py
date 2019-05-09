from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = 'Hello there...'
    my_name = 'Freddie'
    fake_name = 'Testing'
    kwargs = local_vars_to_dict(locals())
    return render(request, 'hello_world.html', kwargs)


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return HttpResponse('<h1>Contact Us</h1>')


def local_vars_to_dict(args):
    prefix = 'my_'
    sourcedict = args
    outputdict = {
        k: sourcedict[k]
        for k in sourcedict
        if k.startswith(prefix)
    }
    return outputdict
