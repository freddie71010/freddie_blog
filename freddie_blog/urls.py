"""freddie_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blog_posts.views import blog_post_create_view
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from searches.views import search_view

from .views import about_page, contact_page, example_page, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', include('blog_posts.urls')),
    path('blog-new/', blog_post_create_view),
    path('search/', search_view),
    # These two are the same thing:
    #       path('blog/<int: post_id>/', blog_post_detail,
    #       re_path('blog/(?P<post_id>\d+/$', blog_post_detail,
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('example/', example_page, name='example'),
    path('fvs-admin/', admin.site.urls)

]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
