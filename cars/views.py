from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CarForm
from .models import Car

class CarPageView(DetailView):
    model = Car
    template_name = "cars/show.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        car = get_object_or_404(Car, pk=pk)
        car.gaz = "да" if car.gaz else "нет"
        return car

class CarPageNew(CreateView):
    form_class = CarForm
    template_name = "cars/new.html"

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.owner = self.request.user
        fields.save()
        return super().form_valid(form)

class CarPageUpdate(UpdateView):
    form_class = CarForm
    template_name = "cars/update.html"

    def get_initial(self):
        initial = super().get_initial()
        initial['transmission'] = self.object.transmission
        initial['air'] = self.object.air
        initial['engine'] = self.object.engine
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Car, pk=pk)