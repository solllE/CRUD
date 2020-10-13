from django.shortcuts import render
from .models import Post

def main(request):
    return render(request, 'main.html')

def new(request):
    return render(request, 'new.html')

def create(requset):
    getTitle = requset.GET.get('title')
    getContent = requset.GET.get('content')

    post = Post(title=getTitle, content=getContent)
    post.save()

    return render(requset, 'create.html')