from django.shortcuts import render
from .models import Post

# This function will haandle the traffic from the home page of the Blog.



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
