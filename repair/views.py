from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView
from .forms import *
from .models import Repair
from cars.models import Car

class RepairPageView(DetailView):
    model = Repair
    template_name = "repair/show.html"

    def get_object(self, queryset=None):
        pk_repair = self.kwargs.get('pk_repair')
        pk_car = self.kwargs.get('pk_car')
        return get_object_or_404(Repair, pk=pk_repair, car__pk=pk_car)

class RepairPageNew(CreateView):
    form_class = RepairForm
    template_name = "repair/new.html"

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.owner = self.request.user
        pk_car = self.kwargs.get('pk_car')
        fields.car = get_object_or_404(Car, pk=pk_car)
        fields.save()
        return super().form_valid(form)