from django.test import TestCase
from django.urls import reverse
from .models import Sheet, Transaction
import datetime


def create_sheet(title, start_date, end_date):
    """
    Create a sheet with the given `title` and with a start and end date
    """
    return Sheet.objects.create(title=title, start_date=start_date, end_date=end_date)


class SheetIndexViewTests(TestCase):
    def test_no_sheets(self):
        """
        If no sheets exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('tracker:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sheets are available for viewing.")
        self.assertQuerysetEqual(response.context['sheet_list'], [])

    def test_1_sheet(self):
        """
        If 1 sheets exist, display the sheet
        """
        create_sheet("December", datetime.date(
            2020, 12, 1), datetime.date(2020, 12, 31))
        response = self.client.get(reverse('tracker:index'))
        self.assertQuerysetEqual(
            list(response.context['sheet_list']),
            ['<Sheet: December>']
        )

    def test_2_sheets(self):
        """
        If 2 sheets exist, display both sheets
        """
        create_sheet("December", datetime.date(
            2020, 12, 1), datetime.date(2020, 12, 31))
        create_sheet("January", datetime.date(
            2021, 1, 1), datetime.date(2021, 1, 31))
        response = self.client.get(reverse('tracker:index'))
        self.assertQuerysetEqual(
            list(response.context['sheet_list']),
            ['<Sheet: December>', '<Sheet: January>']
        )
