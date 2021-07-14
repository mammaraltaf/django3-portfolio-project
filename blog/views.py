from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blogs

# Create your views here.


def all_blog(request):

    # blog = Blogs.objects.order_by('-date')
    # blog = Blogs.objects.order_by('-date')[:5]
    blog = Blogs.objects.all()
    context = {'blog': blog}
    return render(request, 'blog/blogs.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {'id': blog_id, 'blog': blog}
    return render(request, 'blog/detail.html', context)
