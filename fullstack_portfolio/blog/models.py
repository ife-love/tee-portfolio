from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('blog')

    def __str__(self):
        return f'{self.name}'



class Category(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('blog')

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True, default='architecture')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="none")
    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-updated_date', '-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('blog')

    def __str__(self):
        return f'{self.title} | {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.text


# class Blog(models.Model):
#     blog_logo = models.CharField(max_length=255)
#     blog_title = models.TextField()
#     blog_button = models.TextField(max_length=200)
#     blog_bg = models.ImageField()
