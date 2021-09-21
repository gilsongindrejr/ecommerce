from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = get_user_model()
    success_url = reverse_lazy('login')
    form_class = RegisterForm
