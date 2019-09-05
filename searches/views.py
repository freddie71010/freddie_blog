from django.shortcuts import render

from .models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None)
    context = {'query': query}
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
    return render(request, 'searches/view.html', context)
