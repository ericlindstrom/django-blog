import os
from django.db import models

current_app_dir = os.path.split(os.path.dirname(__file__))[1]

#from utils import *
#current_app_dir = get_app_dir(__file__)

class BlogBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    published = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

class BlogCategory(BlogBase):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    @models.permalink
    def get_absolute_url(self):
        return ('blog:category_detail', '', {
            'slug' : self.slug,
        })

class BlogTag(BlogBase):

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    @models.permalink
    def get_absolute_url(self):
        return ('blog:tag_detail', '', {
            'slug' : self.slug,
        })
   

class BlogEntry(BlogBase):
    body = models.TextField()
    date = models.DateTimeField()
    categories = models.ManyToManyField(BlogCategory, blank=True)
    tags = models.ManyToManyField(BlogTag, blank=True)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    @models.permalink
    def get_absolute_url(self):
        return ('blog:entry_detail', '', {
            'year' : self.date.year,
            'month': self.date.strftime('%m'),
            'day'  : self.date.strftime('%d'),
            'slug' : self.slug,
        })


class BlogImage(models.Model):
    entry = models.ForeignKey(BlogEntry)
    image = models.ImageField(upload_to=current_app_dir + '/%Y/%m/%d')

