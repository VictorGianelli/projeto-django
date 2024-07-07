
from django.shortcuts import render

from contact.forms import ContactForm




def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }

    print()
    print(request.method)
    print()

    return render(
        request,
        'contact/create.html',
        context
    )