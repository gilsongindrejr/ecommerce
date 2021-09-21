from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import RegisterForm, AddressForm
from .models import Address


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = get_user_model()
    success_url = reverse_lazy('login')
    form_class = RegisterForm


class AddressView(FormView):
    template_name = 'address.html'
    form_class = AddressForm
    success_url = reverse_lazy('checkout')

    def form_valid(self, form):
        if form.is_valid():
            address = Address()
            address.zip_code = form.cleaned_data['zip_code']
            address.address = form.cleaned_data['address']
            address.house_number = form.cleaned_data['house_number']
            address.complement = form.cleaned_data['complement']
            address.neighborhood = form.cleaned_data['neighborhood']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.save()
            self.request.user.address = address
            self.request.user.save()
        return super(AddressView, self).form_valid(form)
