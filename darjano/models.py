from django.db import models
from django import forms
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Branch(models.Model):
    choice = [('1','1'),('2','2'),('3','3')]
    branch_no = models.CharField(max_length=2,choices=choice)

    def __str__(self):
        return self.branch_no

class Salon(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    address = models.TextField()
    branch = models.OneToOneField(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = '__all__'

def unique_slug_generator(model_instance,name,slug_field):
    slug = slugify(name)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk +1
        slug = f'{slug}-{object_pk}'

    return slug

def slug_save(sender, instance, *args, **kwargs):
    # if not instance.slug:
    instance.slug = unique_slug_generator(instance,instance.name, instance.slug)
pre_save.connect(slug_save,sender=Salon)