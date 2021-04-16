from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .forms import LinkForm
from .models import Link
from .b62 import base_encode, base_decode

def url(request, short_url):
    link = Link.objects.filter(short_url=short_url)
    return redirect(link.long_url)

class HomeView(CreateView, ListView):
    model = Link
    form_class = LinkForm
    template_name = 'home.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        if not Link.objects.last():
            counter = 999999999999
        else:
            last_url = Link.objects.last().short_url
            last_url = base_decode(last_url)
            counter = int(last_url) - 1

        context['short_url_encode'] = base_encode(counter)
        return context