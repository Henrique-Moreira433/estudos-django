from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('blog')
    context ={ 
    'text': 'ESTAMOS NO BLOG ',
    'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    context ={ 
    'text': 'ESTAMOS NO EXEMPLO ',
    'title': 'titulo meu',
    }
    return render(
        request,
        'blog/exemplo.html',
        
        context
    )
    


def post(request, _id):
    found_post = None

    for post in posts:
        if post ['id'] == _id:
            found_post = post
            break

    context ={ 
    'text': 'ESTAMOS NO POST ',
    'posts': [found_post]
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    context ={ 
    'text': 'ESTAMOS NO EXEMPLO ',
    'title': 'titulo meu',
    }
    return render(
        request,
        'blog/exemplo.html',
        
        context
    )