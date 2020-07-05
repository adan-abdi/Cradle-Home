from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


from .models import Post

# Create your views here.

# display homepage
def home(request):
    # data to be passed to context
    # profile details, featured projects, filter latest articles=3, contact me, testimonials, blog newsletter list
    context = {}
    return render(request, 'index.html', context)


# def blog(request):
#     # data to be passed
#     # blog newsletter, Blog-list/Posts,
#     context = {}
#     return render(request, 'blog-list.html', context)

# def blogdetail(request):
#     # data to be passed to context
#     # Profile, Blog newsletter, tags, related articles Blog details; BannerImg, Meta, Content, Comments, Reply form
#     context = {}
#     return render(request, 'blog-detail.html', context)



# display all posts
def post_list(request):
    # request parameter is required by all views
    # retrieve all the posts with the published status using the published manager 
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    # get the page GET parameter, which indicates the current page number
    page = request.GET.get('page')
    try:
        # obtain the objects for the desired page by calling the page() method of Paginator
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    # pass the page number (page) and retrieved objects (posts) to the template
    return render(request,
                 'blog-list.html',
                 {'page': page,
                  'posts': posts})


# takes in year, month, day, and post to query a details of a single post
def post_detail(request, year, month, day, post):
    # get a post object or 404 error
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog-detail.html',
                  {'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog-list.html'