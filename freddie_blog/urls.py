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
from blog_posts.views import blog_post_detail
from django.contrib import admin
from django.urls import path

from .views import about_page, contact_page, example_page, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_post_detail),
    path('blog/<str:slug>/', blog_post_detail),
    # These two are the same thing:
    #       path('blog/<int: post_id>/', blog_post_detail,
    #       re_path('blog/(?P<post_id>\d+/$', blog_post_detail,
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('example/', example_page, name='example'),
    path('fvs-admin/', admin.site.urls),

]
