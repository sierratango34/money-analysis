from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Sheet, Transaction

class IndexView(generic.ListView):
    template_name = "tracker/index.html"
    context_object_name = "sheet_list"

    def get_queryset(self):
        """Return all of the sheets"""
        return Sheet.objects.all()

class SheetDetailView(generic.DetailView):
    model = Sheet
    template_name = "tracker/sheet-detail.html"

# class TransactionDetailView(generic.DetailView):
#     model = Transaction
#     template_name = "tracker/transaction-detail.html"


