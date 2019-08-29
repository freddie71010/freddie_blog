from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    """
    blogpost_set --> queryset related to the user

    Example:
    j = User.objects.first() --> <User: fvs>
    j.blogpost_set.all() -->
    <QuerySet [<BlogPost: Galaxy S6>, <BlogPost: Part 8 of The Sleeping Sheep>, <BlogPost: Hello World>]
    """
    # id = models.IntegerField() # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    def get_edit_url(self):
        return f'{self.get_absolute_url}/edit/'

    def get_delete_url(self):
        return f'{self.get_absolute_url}/delete/'
