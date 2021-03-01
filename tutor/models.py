from django.db import models
from webapp import settings
from django.db import models
from django.db.models import Avg
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from tutor.fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils import timezone
from autoslug import AutoSlugField
from .fields import OrderField

from PIL import Image






class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=400)


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

class Course(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=400,unique=True)
    description =models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField(default=0.1)
    image = models.ImageField(upload_to="thumbnails")
    
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


    def __str__(self):
        return str(self.title)


    class Meta:
        ordering = ('-date_created',)

 # def course_rating(self.rate):
    #     self.rate = Review.

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules',on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=400,unique=True)
    numbering = models.IntegerField(default=1)
    order = OrderField(blank=True, for_fields=['course'])

    
    

    def __str__(self):
        return f'{self.order}. {self.title}'


    class Meta:
        ordering = ['order']


class Text(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=250)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='files')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    document = models.ImageField(upload_to='images')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents',on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
     limit_choices_to={'model__in':('text', 'video', 'image', 'file')},
        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    numbering = models.IntegerField(default=1)
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        
        ordering = ['order']


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    course = models.ForeignKey(Course, related_name='reviews',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviewers',on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

