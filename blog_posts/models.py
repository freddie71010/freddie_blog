from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField()  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
