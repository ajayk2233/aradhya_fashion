from django.db import models
from django import forms

class Branch(models.Model):
    choice = [('1','1'),('2','2'),('3','3')]
    branch_no = models.CharField(max_length=2,choices=choice)

    def __str__(self):
        return self.branch_no

class Salon(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    branch = models.OneToOneField(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = '__all__'