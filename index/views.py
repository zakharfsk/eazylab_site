from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'EazyLab',
        'user': request.user,
        'status': False
    }

    return render(request, 'index/index.html', context)
