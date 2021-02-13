import datetime
from django.db import models
from django.utils import timezone

class Sheet(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')

    def __str__(self):
        return self.title

    def is_currently_active(self):
        today = timezone.localtime(timezone.now()).date()
        return self.end_date >= now


class Transaction(models.Model):
    GENERAL = 'general'
    GROCERIES = 'groceries'
    SHOPPING = 'shopping'
    ENTERTAINMENT = 'entertainment'
    EATING_OUT = 'eating_out'
    PERSONAL_CARE = 'personal_care'
    CHARITY = 'charity'
    SAVINGS = 'savings'
    GIFTS = 'gifts'
    TRANSPORT = 'transport'
    HOLIDAY = 'holiday'
    FAMILY = 'family'
    DEBT = 'debt'
    BILLS = 'bills'
    FINANCES = 'finances'
    FUEL = 'fuel'

    CATEGORY_CHOICES = [
        (GENERAL, 'General'),
        (GROCERIES, 'Groceries'),
        (SHOPPING, 'Shopping'),
        (ENTERTAINMENT, 'Entertainment'),
        (EATING_OUT, 'Eating Out'),
        (PERSONAL_CARE, 'Personal Care'),
        (CHARITY, 'Charity'),
        (SAVINGS, 'Savings'),
        (GIFTS, 'Gifts'),
        (TRANSPORT, 'Transport'),
        (HOLIDAY, 'Holiday'),
        (FAMILY, 'Family'),
        (DEBT, 'Debt'),
        (BILLS, 'Bills'),
        (FINANCES, 'Finances'),
        (FUEL, 'Fuel'),
    ]

    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=GENERAL)
    amount = models.IntegerField(default=0)
    date = models.DateField('date')


    def __str__(self):
        return self.description