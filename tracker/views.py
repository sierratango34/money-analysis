from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Sheet, Transaction
from .forms import TransactionForm

class IndexView(generic.ListView):
    template_name = "tracker/index.html"
    context_object_name = "sheet_list"

    def get_queryset(self):
        """Return all of the sheets"""
        return Sheet.objects.all()

def sheetDetail(request, sheet_id):
    form = TransactionForm()
    sheet = get_object_or_404(Sheet, pk=sheet_id)

    context = {
        'sheet': sheet,
        'form': form
    }
    return render(request, 'tracker/sheet-detail.html', context)

# class TransactionDetailView(generic.DetailView):
#     model = Transaction
#     template_name = "tracker/transaction-detail.html"

def addTransaction(request, sheet_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/<int:pk>/')

    else:
        form = TransactionForm()

    return render(request, 'tracker/new-transaction-form.html', {'form': form})

