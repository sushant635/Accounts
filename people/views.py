from django.shortcuts import render

# Create your views here.
from app.mixins import (
    RestrictToSelectedOrganizationQuerySetMixin,
    AutoSetSelectedOrganizationMixin)
from .models import Client, Employee
from .forms import ClientForm, EmployeeForm
from django.urls import reverse,reverse_lazy


class ClientListView(RestrictToSelectedOrganizationQuerySetMixin,
                     generic.ListView):
    template_name = "client_list.html"
    model = Client
    context_object_name = "clients"


class ClientCreateView(AutoSetSelectedOrganizationMixin,
                       generic.CreateView):
    template_name = "client_create_or_update.html"
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("people:client-list")


class ClientUpdateView(RestrictToSelectedOrganizationQuerySetMixin,
                       AutoSetSelectedOrganizationMixin,
                       generic.UpdateView):
    template_name = "client_create_or_update.html"
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("people:client-list")


class ClientDetailView(RestrictToSelectedOrganizationQuerySetMixin,
                       generic.DetailView):
    template_name = "client_detail.html"
    model = Client
    context_object_name = "client"


class EmployeeListView(RestrictToSelectedOrganizationQuerySetMixin,
                       generic.ListView):
    template_name = "employee_list.html"
    model = Employee
    context_object_name = "employees"


class EmployeeCreateView(AutoSetSelectedOrganizationMixin,
                         generic.CreateView):
    template_name = "employee_create_or_update.html"
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("people:employee-list")


class EmployeeUpdateView(RestrictToSelectedOrganizationQuerySetMixin,
                         AutoSetSelectedOrganizationMixin,
                         generic.UpdateView):
    template_name = "employee_create_or_update.html"
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("people:employee-list")


class EmployeeDetailView(RestrictToSelectedOrganizationQuerySetMixin,
                         generic.DetailView):
    template_name = "employee_detail.html"
    model = Employee
    context_object_name = "employee"