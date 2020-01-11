from django.urls import path
from . import views

app_name = 'bluApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('transact/', views.transact, name='transact'),
    path('loan/', views.loan, name='loan'),
    path('aplica-credito/', views.aplica_credito, name='aplica_credito')


]