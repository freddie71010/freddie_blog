from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = 'Hello there...'
    my_name = 'Freddie'
    fake_name = 'Testing'
    title = 'Hello Worlddd'
    my_list = [1, 2, 3, 4]
    kwargs = local_vars_to_dict(locals())
    return render(request, 'home.html', kwargs)


def about_page(request):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


def contact_page(request):
    return render(request, 'about.html', {'title': 'Contact'})


def example_page(request):
    context = {'title': 'Example page'}
    template_name = 'hello_world.html'
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))


def local_vars_to_dict(args):
    sourcedict = args
    outputdict = {k: sourcedict[k] for k in sourcedict}
    return outputdict
