from django.urls import path,  register_converter
from datetime import datetime
from .views import *

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')


urlpatterns = [
    path('', index, name='index'),
    path('creare-client/', create_client_ro, name='create-client'),
    path('creare-client-ro/', create_client_ro, name='create-client-ro'),
    path('creare-client-strain/', create_client_strain, name='create-client-strain'),
    path('creare-valuta/', create_valuta, name='create-valuta'),
    path('creare-cotatie/', create_cotatie, name='create-cotatie'),
    path('creare-schimb/', create_schimb, name='create-schimb'),



    path('lista-clienti/', client_list, name='client-list'),
    path('lista-valute/', valuta_list, name='valuta-list'),
    path('lista-cotatii/', cotatie_list, name='cotatie-list'),
    path('lista-schimburi/', schimb_list, name='schimb-list'),
    path('registru-zilnic/', schimb_list_date, name='schimb-list-date'),




    path('edit-client/<int:id>', edit_client, name='edit-client'),
    path('edit-valuta/<int:id>', edit_valuta, name='edit-valuta'),
    path('edit-cotatie/<int:id>', edit_cotatie, name='edit-cotatie'),
    path('edit-schimb/<int:id>', edit_schimb, name='edit-schimb'),

    path('delete-client/<int:id>', delete_client, name='delete-client'),
    path('delete-valuta/<int:id>', delete_valuta, name='delete-valuta'),
    path('delete-cotatie/<int:id>', delete_cotatie, name='delete-cotatie'),
    path('delete-schimb/<int:id>', delete_schimb, name='delete-schimb'),


]