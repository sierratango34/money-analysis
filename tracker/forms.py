from django import forms
from .models import Sheet, Transaction

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


class TransactionForm(forms.Form):
    description = forms.CharField(max_length=200)
    category = forms.CharField(max_length=30)
    amount = forms.IntegerField()
    date = forms.DateField(widget=forms.SelectDateWidget())
    category = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=CATEGORY_CHOICES,
    )

    def clean_description(self):
        data = self.cleaned_data['description']

        data.strip()

    # def clean_category(self)
