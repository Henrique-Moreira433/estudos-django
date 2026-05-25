from django.shortcuts import render


def home(request):
    print('home')
    context ={ 
    'text': 'ESTAMOS NA HOME '
    }

    return render(
        request,
        'home/index.html',
        context
        
    )
