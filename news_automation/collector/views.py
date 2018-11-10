from django.shortcuts import render
from collector.forms import ContactForm


# Create your views here.
def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })