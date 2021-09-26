from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class department(models.Model):
    dep_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    # image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('dep_name',)
        verbose_name='department'
        verbose_name_plural='department'
    def get_url(self):
        return reverse("dapp:products_by_category",args=[self.slug])
    def __str__(self):
        return '{}'.format(self.dep_name)


class docters(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    category=models.ForeignKey(department,on_delete=models.CASCADE)



    def get_url(self):
         return reverse("dapp:ProCatDetail",args=[self.category.slug,self.slug])

    def __str__(self):
         return '{}'.format(self.name)

class appoinment(models.Model):
    name = models.CharField(max_length=250,blank=True)
    email = models.EmailField(max_length=70,blank=True)
    phone = models.IntegerField(max_length=10)
    date = models.DateField(auto_now_add=True)
    departments = models.CharField(max_length=25,blank=True)
    doctor = models.CharField(max_length=25,blank=True)
class Task(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)