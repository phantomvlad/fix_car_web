from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .forms import CarForm
from .models import Car
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

@method_decorator(login_required,name='dispatch')
class CarPageList(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(owner=user).order_by('-time_update')
