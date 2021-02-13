from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SheetDetailView.as_view(), name='detail'),
]