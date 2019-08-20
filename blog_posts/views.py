from django.http import Http404
from django.shortcuts import render

from .models import BlogPost


def blog_post_detail(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    obj = queryset.first()
    # queryset = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)
