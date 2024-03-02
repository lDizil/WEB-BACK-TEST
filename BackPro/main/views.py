from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница!',
        'values': ['Some', 'Hello', '245'],
        'obj': {
            'car': 'BMW',
            'age': '18',
            'hobby': 'Volleyball'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
