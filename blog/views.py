from django.shortcuts import render

def blog(request):
    print('blog')
    context ={ 
    'text': 'ESTAMOS NO BLOG '
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