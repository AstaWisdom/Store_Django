from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post, Comment
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from Thoth_Gaming.models import Order
from Thoth_Gaming.utils import cartcookies
from django.http.response import Http404
# Create your views here.


def homepage(request):

    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        cartitems = order.cart_total_items
    else:
        Cookiedata = cartcookies(request)
        cartitems = Cookiedata['cartitems']

    query = ""

    if request.GET:
        try:
            query = request.GET['search']
        except:
            pass

    posts_pages = blog_search(query)
    paginator = Paginator(posts_pages, 5)

    page_num = request.GET.get('page')


    posts = paginator.get_page(page_num)

    context = {'posts': posts, 'query': str(query), 'cartitems': cartitems}
    return render(request, 'Blog/homepage.html', context)


def post(request, slug):
    # For cart items on navbar counting
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        cartitems = order.cart_total_items
    else:
        Cookiedata = cartcookies(request)
        cartitems = Cookiedata['cartitems']
    # The actualy Post
    posts = Post.objects.get(slug=slug)
    try:
        comments = Comment.objects.filter(post=posts)
    except:
        comments = ''

    if request.method == 'POST':
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            post = Post.objects.get(slug=slug)
            comment = request.POST['Comment']
            Comment(text=comment, post=post, user=user).save()
    context = {'posts': posts, 'comments': comments, 'cartitems': cartitems}
    return render(request, 'Blog/post.html', context)

def blog_search(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(category__icontains=q)).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))
