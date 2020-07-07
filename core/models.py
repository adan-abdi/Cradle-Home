from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# If you delacre a custom model manager like the one below but you want to keep the objects as default, you have to add objects explicityly in the model
class PublishedManager(models.Manager):
    def get_queryset(self):
        #returns the QuerySet that will be executed. You override this method to include your custom filter in the final QuerySet
        # This returns objects filtered by a publish status
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    # Posts model
    # Posts have status of draft or published and only published posts are displayed publicly
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    banner = models.ImageField(max_length=255, upload_to="banners", null=True, blank=True)
    title = models.CharField(max_length=250)
    # Used for dynamic urls in post-detail view, the slug has unique_for_date parameter to build urls slugs using the publish date and slug. Posts also have unique slugs
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # author defines a many-to-one relationship with posts. When deleted all related posts are deleted due to the SQL standard CASCADE. The name of the reverse relationship from user to post with related_name attr to allow access of related objects easily
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # TODO: Post body, split to Intro, Body and Conclusion Later
    # Add banner Image, offer placeholder dimensions if possible
    intro = models.TextField()
    body = models.TextField()
    conclusion = models.TextField()
    # timezone.now is like a timezone aware version of datetime.now method.
    publish = models.DateTimeField(default=timezone.now)
    # by default, posts create date are started form the moment an instance of post is created
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # first manager declared in a model becomes the default manager, you can use the Meta attr default_manager_name to specify a different manager
    # retreives using Post.objects.all()
    objects = models.Manager() # The default manager of every model that retrieves all objects in the database
    # retreives using Post.published.all()
    published = PublishedManager() # Our custom manager to retreive all posts with published status
    tags = TaggableManager() # taggable manager to add tags to this model

    class Meta:
        '''order by published date from latest'''
        ordering = ('-publish',)
        

    def __str__(self):
        return self.title

    #convention in Django is to add a get_absolute_url() method to the model that returns the canonical URL for the object.
    def get_absolute_url(self):
        return reverse('core:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])


# Comment System
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


# Newsletter List
# class Newsletter(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='newsletter', null=True)
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     subscribed = models.BooleanField(default=True)
#     subscribedwhen = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-subscribedwhen',)

#     def __str__(self):
#         return self.name


# class SharedPost(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='share', null=True)
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     recipientemail = models.EmailField()
#     message = models.TextField(null=True, blank=True)
#     shared = models.DateTimeField(auto_now_add=True)
#     sent  = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('-shared',)

#     def __str__(self):
#         return self.name