from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import BlogPostModelForm
from .models import BlogPost


def blog_post_list_view(request):
    # list out objects, could also be a search view
    qs = BlogPost.objects.all()
    template_name = 'blog_posts/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # Returns 1 object or a detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
