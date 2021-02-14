from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:sheet_id>/', views.sheetDetail, name='sheet_detail'),
    path('<int:sheet_id>/addtransaction/', views.addTransaction, name='add_transaction'),
]