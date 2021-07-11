from django.shortcuts import render

# This function will haandle the traffic from the home page of the Blog.


posts = [
    {
        'author': 'Patrick O Rourke',
        'title' : 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'July 10, 2021'

    },
{
        'author': 'Britany Spears',
        'title' : 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July 11, 2021'

    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
