from django.contrib import admin
from .models import Invoice, InvoiceDetail

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'date', 'customer_name')
    list_filter = ('date', 'customer_name')
    search_fields = ('invoice_no', 'customer_name')

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'price')
    list_filter = ('invoice', 'description')
    search_fields = ('invoice__invoice_no', 'description')  # Searching by invoice number
