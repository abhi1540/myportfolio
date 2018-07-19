from django.db import models
import os
import random
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,10000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    tag = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def get_url(self):
        return reverse('blog:categories', args=[self.tag])


    class Meta:
        ordering = ('created',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Category)
