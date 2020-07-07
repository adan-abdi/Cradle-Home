from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count


from .forms import CommentForm
from .models import Post, Comment, Profile

# Create your views here.

# display homepage
def home(request):
    active_profile = Profile.objects.filter(status=True).first()
    context = {
                'active_profile': active_profile,
    }
    return render(request, 'index.html', context)


# display all posts
def post_list(request,  tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])


    paginator = Paginator(object_list, 6)
    # get the page GET parameter, which indicates the current page number
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {
                'page': page, 
                'posts': posts,
                'tag': tag
            }
    return render(request, 'blog-list.html', context)



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    # Comment System on blog-detail
    if request.method == 'POST':
        # Comment form
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]


    context = {
                'post': post, 
                'comments': comments, 
                'new_comment': new_comment, 
                'comment_form': comment_form,
                'similar_posts': similar_posts
            }
    return render(request, 'blog-detail.html', context)


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog-list.html'
