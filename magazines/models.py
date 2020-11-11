from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null =True)
    email = models.CharField(max_length=200, null =True)
    data_created = models.DateTimeField(auto_now_add=True, null =True)

    def __str__(self):
        return self.name

 

class Magazine(models.Model):
   

    name = models.CharField(max_length=200, null =True)
    description = models.CharField(max_length=300, null =True) 
    feature = models.CharField(max_length=300, null =True)
    magazineGroup = models.CharField(max_length=50, null = True)
    pdf = models.FileField(null =True, blank = True)
    thumbNail = models.FileField(null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    viewcount = models.PositiveIntegerField(default=0)


    @property
    def update_viewcount(self):
        self.viewcount = self.viewcount + 1
        self.save()
        return ''


    def save(self, *args, **kwargs):
        super(Magazine, self).save(*args, **kwargs)
        filename = self.pdf.url
        thumbNailLink = self.thumbNail.url

    def __str__(self):
        return self.name
    


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    involvedEditor = models.TextField(blank=True)
    image = models.FileField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    viewcount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def update_viewcount(self):
        self.viewcount = self.viewcount + 1
        self.save()
        return self.viewcount

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'static/images/posts')

    def __str__(self):
        return self.post.title
