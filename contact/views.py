from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact(request):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jajeuff wayy 👍(Message envoyer avec succes)')
            return redirect('/contact/')

    context = {'form': form}
    return render(request, 'contact/formulaire.html', context)
