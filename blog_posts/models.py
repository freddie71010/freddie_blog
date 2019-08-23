from django.db import models


class BlogPost(models.Model):
    # id = models.IntegerField() # pk
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
