from typing import Iterable
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class NewsContext(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    slug = models.SlugField(unique=True)

    is_published = models.BooleanField(default=False)
    publish_time = models.DateTimeField()
    creat_at = models.DateTimeField(auto_now=True)


    def save(self,*args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
       
