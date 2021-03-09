from django.db import models
from webapp import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to = 'post_images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="post_user",on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class File(models.Model):
    title = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='files')

    def __str__(self):
        return self.title



class Image(models.Model):
    title = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='files')

    def __str__(self):
        return self.title



class Text(models.Model):
    title = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title



class Video(models.Model):
    title = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()

    def __str__(self):
        return self.title