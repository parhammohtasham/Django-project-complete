from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcom to my blog</h1>')

def post_list(request):
    posts=Post.published.all()
    paginator=Paginator(posts,2)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,'blog/list.html',{'posts':posts , 'page':page})

# class PostListView(ListView):
#     queryset=Post.published.all()
#     context_object_name='posts'
#     paginate_by=2
#     template_name='blog/list.htnl'

def post_detail(request,pk,slug,year,month,day):
    post=get_object_or_404(Post,status='published',id=pk,slug=slug,publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/detail.html',{'post':post})