from django.db import models
# from django.db import models
# from django.utils import timezone
# from django.urls import reverse
# from django.contrib.auth.models import User


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         # The get_queryset() method of a manager returns the QuerySet that will be executed. You override this method to include your custom filter in the final QuerySet
#         return super().get_queryset().filter(status='published')


# class Post(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250,
#                             unique_for_date='publish')
#     author = models.ForeignKey(User,
#                               on_delete=models.CASCADE,
#                               related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10,
#                               choices=STATUS_CHOICES,
#                               default='draft')
#     # retreives using Post.objects.all()
#     objects = models.Manager() # The default manager tof every model that retrieves all objects in the database
#     # retreives using Post.published.all()
#     published = PublishedManager() # Our custom manager to retreive all posts with published status

#     class Meta:
#         '''order by published date from latest'''
#         ordering = ('-publish',)
        

#     def __str__(self):
#         return self.title

#     #convention in Django is to add a get_absolute_url() method to the model that returns the canonical URL for the object.
#     def get_absolute_url(self):
#         return reverse('blog:post_detail',
#                        args=[self.publish.year,
#                              self.publish.month,
#                              self.publish.day, self.slug])