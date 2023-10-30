from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def index(request):
    myObject = Post.objects.all().first()
    return render(request,'posts/index.html',{'post':myObject})

def single(request, post_id):
    return render(request,'posts/single.html', {'single':post_id})
