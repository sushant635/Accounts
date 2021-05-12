from django.forms import ModelForm
from django.contrib.auth import get_user_model

from .models import Client, Employee

# from django_select2 import fields as s2forms
# from django_select2.fields import (
#     AutoModelSelect2Field,
#     AutoModelSelect2MultipleField)
# from django_select2.fields import AutoModelSelect2Field

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = (
            "name",
            "address_line_1",
            "address_line_2",
            "city",
            "postal_code",
            "country",
        )

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "email",

            "payroll_tax_rate",

            "salary_follows_profits",
            "shares_percentage",

        )

User = get_user_model()

# class UserChoices(s2forms.AutoModelSelect2Field):
# # class UserChoices(ModelForm):

#     queryset = User.objects.all()
#     search_fields = (
#         'first_name__icontains',
#         'last_name__icontains',
#         'username__icontains',
#         'email__icontains',
#     )

# class UserMultipleChoices(s2forms.AutoModelSelect2MultipleField):
# # class UserMultipleChoices(ModelForm):
#     queryset = User.objects.all()
#     search_fields = (
#         'first_name__icontains',
#         'last_name__icontains',
#         'username__icontains',
#         'email__icontains',
#     )