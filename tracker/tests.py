from django.test import TestCase
from django.urls import reverse
from .models import Sheet, Transaction


class SheetIndexViewTests(TestCase):
    def test_no_sheets(self):
        """
        If no sheets exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('tracker:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sheets are available for viewing.")
        self.assertQuerysetEqual(response.context['sheet_list'], [])
