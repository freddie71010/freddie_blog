from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    # id = models.IntegerField() # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
