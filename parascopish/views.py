from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    
    posts = Post.objects.all()
    return render(request, 'parascopish/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()
    return render(request, 'parascopish/post_detail.html', {'post': post, 'posts': posts})
    