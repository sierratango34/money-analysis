from django.contrib import admin

from .models import Sheet, Transaction

# class SheetAdmin(models.ModelAdmin):


# class TransactionAdmin(models.ModelAdmin):



admin.site.register(Sheet)
admin.site.register(Transaction)