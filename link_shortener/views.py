from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .forms import LinkForm
from .models import Link
from .b62 import base_encode, base_decode
from braces.views import LoginRequiredMixin

def url(request, short_url):
    link = Link.objects.get(short_url=str(short_url))
    return redirect(link.long_url)

class HomeView(LoginRequiredMixin, CreateView, ListView):
    model = Link
    form_class = LinkForm
    template_name = 'home.html'
    login_url = '/users/login/'

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

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(HomeView, self).dispatch(*args, **kwargs)