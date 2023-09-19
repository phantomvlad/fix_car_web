
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView
from django.http import request

from .models import Car

class CarPageView(DetailView):
    model = Car
    template_name = "cars/show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        car = get_object_or_404(Car, pk=pk)
        context['car'] = car
        return context


class CarPageNew(CreateView):
    model = Car
    fields = "__all__"
    template_name = "cars/new.html"