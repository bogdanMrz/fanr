from django.db import models
from django.utils import timezone

# Create your models here.


class Client(models.Model):
    
    numar_document = models.IntegerField(unique=True)
    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=50)
    data_nasterii = models.DateField()
    adresa = models.CharField(max_length=100, blank=True, null=True)
    tara = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.nume} {self.prenume}'



class Valuta(models.Model):
    nume = models.CharField(max_length=20)
    tara = models.CharField(max_length=100)
    sold = models.FloatField()
    
    def __str__(self):
        return f'{self.nume} {self.tara}'


class Cotatie(models.Model):
    valuta = models.ForeignKey('Valuta', on_delete=models.CASCADE)
    curs_cumparare = models.FloatField()
    curs_vanzare = models.FloatField()
    data = models.DateField()
    ora = models.TimeField()

    def __str__(self):
        return f'{self.valuta} {self.data.year}-{self.data.month}-{self.data.day} {self.ora.hour}:{self.ora.minute}'


class BuletinDeSchimb(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    cotatie = models.ForeignKey('Cotatie', on_delete=models.CASCADE)
    
    TIP = [
        ('C','Cumparare'),
        ('V', 'Vanzare'),
    ]

    tip = models.CharField(choices=TIP, max_length=2)
    
    data = models.DateField()
    ora = models.TimeField()

    suma_valuta = models.FloatField()
    suma_lei = models.FloatField()


    def __str__(self):
        return f'{self.id} {self.data.year}-{self.data.month}-{self.data.day} {self.ora.hour}:{self.ora.minute} {self.cotatie.valuta} {self.suma_lei}RON {self.suma_valuta}'




class Zi(models.Model):
    pass