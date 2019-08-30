from blog_posts.models import BlogPost
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {'title': 'Welcome to FVS Blog', 'blog_list': qs}
    return render(request, 'home.html', context)


def about_page(request):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {'title': 'Contact',
               'form': form
               }
    return render(request, 'form.html', context)


def example_page(request):
    context = {'title': 'Example page'}
    template_name = 'hello_world.html'
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))


def local_vars_to_dict(args):
    sourcedict = args
    outputdict = {k: sourcedict[k] for k in sourcedict}
    return outputdict
