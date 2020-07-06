from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail


from .forms import SharedPostForm, CommentForm, NewsletterList
from .models import Post, Comment, Newsletter

# Create your views here.

# display homepage
def home(request):
    context = {}
    return render(request, 'index.html', context)



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
    context = {'page': page, 'posts': posts}
    return render(request, 'blog-list.html', context)


# takes in year, month, day, and post to query a details of a single post
def post_detail(request, year, month, day, post):
    shared_form = SharedPostForm()
    newsletter_form = NewsletterList()
    # get a post object or 404 error
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    newsletter = post.newsletter.filter(subscribed=True)
    # sharedpost = post.sharedpost.filter(sent=True)

    new_comment = None
    user_subscribed = None
    share_success = None


    if request.method == 'POST':
        # A Form was submitted
        # Share form
        shared_form = SharedPostForm(data=request.POST)
        if shared_form.is_valid():
            share_success = shared_form.save(commit=False)
            share_success.post = post
            shared_form.save()
    else:
        shared_form = SharedPostForm()

    # TODO: add user to Newsletter model with anonymous auth
    if request.method == 'POST':
        # A Form was submitted
        # Newsletter form
        newsletter_form = NewsletterList(data=request.POST)
        if newsletter_form.is_valid():
            # TODO: Filter the submitted data to check if email, or name have already been subscribed to the newsletter
            user_subscribed = newsletter_form.save(commit=False)
            user_subscribed.post = post
            newsletter_form.save()
    else:
        newsletter_form = NewsletterList()


    if request.method == 'POST':
        # A Form was submitted
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

    context = {
                'SharedPost': SharedPost,
                'share_success': share_success,
                'shared_form': shared_form,
                'newsletter': newsletter,
                'user_subscribed': user_subscribed,
                'newsletter_form': newsletter_form,
                'post': post, 
                'comments': comments, 
                'new_comment': new_comment, 
                'comment_form': comment_form
            }
    return render(request, 'blog-detail.html', context)


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog-list.html'


# Form Views
# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Post, id=post_id, status='published')
#     sent = False
#     form = EmailPostForm(request.POST)

#     if request.method == 'POST':
#         # Form was submitted

#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             # ... send email
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"{cd['name']} recommends you read " f"{post.title}"
#             message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
#             send_mail(subject, message, 'adanabdi036@gmail.com', [cd['to']])
#             sent = True
#         else:
#             form = EmailPostForm()
#     context = {
#                 'post': post,
#                 'form': form
#                 }
#     return render(request, 'blog-share.html', context)