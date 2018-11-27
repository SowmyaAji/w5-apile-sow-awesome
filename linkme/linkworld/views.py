from django.shortcuts import render
from linkworld.models import Post

def index(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, 'index.html', {'posts': posts, })
