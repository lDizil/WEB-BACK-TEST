from django.shortcuts import render, redirect
from .models import Data
from .forms import DataForm
from django.views.generic import DetailView, UpdateView, DeleteView



class AccDetail(DetailView):
    model = Data
    template_name = 'acc/details_acc.html'
    context_object_name = 'article'


class AccUpdateView(UpdateView):
    model = Data
    template_name = 'acc/create.html'

    form_class = DataForm

class AccDeleteView(DeleteView):
    model = Data
    success_url = '/account/'
    template_name = 'acc/acc-delete.html'



def acc_home(request):
    acc = Data.objects.order_by('Login')  # [:3] срез записей
    return render(request, 'acc/acc_home.html', {'acc': acc})

def create(request):
    error = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = DataForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'acc/create.html', data)
