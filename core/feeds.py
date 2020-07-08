from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy


from .models import Post






class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('core:post_list')
    description = 'New articles of my blog.'


    def items(self):
        return Post.published.all()[:3]


    def item_title(self, item):
        return item.title


    def item_description(self, item):
        return truncatewords(item.body, 20)

