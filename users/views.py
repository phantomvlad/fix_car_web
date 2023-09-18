from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import CustomUser

class UserPageView(DetailView):
    model = CustomUser
    template_name = "users/show.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        account = get_object_or_404(CustomUser, pk=pk)
        cars = account.cars.all()
        context['account'] = account
        context['cars'] = cars
        return context
