from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView
from .forms import CarForm
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
    form_class = CarForm
    template_name = "cars/new.html"

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.owner = self.request.user
        fields.save()
        return super().form_valid(form)