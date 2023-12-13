from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, FormView
from .models import CustomUser
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

class UserPageView(DetailView):
    model = CustomUser
    template_name = "users/show.html"