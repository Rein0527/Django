from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import CustomerModelForm
# Create your views here.

def index(request):

    form = CustomerModelForm()

    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')

    context = {
        'form': form
    }

    return render(request, 'customer/index.html', context)
