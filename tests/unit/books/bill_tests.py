from decimal import Decimal as D

from django.test import TestCase

from django_dynamic_fixture import G
import mock

from app.models import Bill


class TestBillQuerySetMethods(TestCase):

    def setUp(self):
        pass

    def test_returns_correct_turnovers(self):
        invoice1 = G(Bill,
            number=101,
            total_excl_tax=D('10.00'),
            total_incl_tax=D('12.00'))

        invoice2 = G(Bill,
            number=102,
            total_excl_tax=D('5.00'),
            total_incl_tax=D('6.00'))

        queryset = Bill.objects.all()
        self.assertEqual(queryset.debts_excl_tax(), D('10.00') + D('5.00'))
        self.assertEqual(queryset.debts_incl_tax(), D('12.00') + D('6.00'))
