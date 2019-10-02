from django.db import models
from django.contrib.auth.models import User
from configuration.models import Social
# Create your models here.


class Category(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Category"
	    verbose_name_plural = "Categories"

	def __str__(self):
	    return '{}'.format(self.titre)


class Plat(models.Model):
	# TODO: Define fields here
	name = models.CharField(max_length=100,null=True)
	prix = models.PositiveIntegerField()
	image = models.ImageField(upload_to='restaurant/plat')
	ingredient = models.ManyToManyField('Ingredient',related_name='plat_ingredient')
	category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_plat')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Plat"
	    verbose_name_plural = "Plats"

	def __str__(self):
	    return '{}'.format(self.name)


class Chef(models.Model):
	# TODO: Define fields here
	first_name = models.CharField(max_length=50,null=True)
	last_name = models.CharField(max_length=50,null=True)
	image = models.ImageField(upload_to='restaurant/chef')
	poste = models.ForeignKey('Poste',on_delete=models.CASCADE,related_name='poste_chef')
	social = models.ManyToManyField(Social,related_name='social_chef')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Chef"
	    verbose_name_plural = "Chefs"

	def __str__(self):
	    return '{} {}'.format(self.first_name,self.last_name)

class Reservation(models.Model):
	# TODO: Define fields here
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=50)
	date = models.DateTimeField()
	person = models.IntegerField()
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
	    verbose_name = "Reservation"
	    verbose_name_plural = "Reservations"

	def __str__(self):
	    return '{}'.format(self.name)

class Poste(models.Model):
	titre = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Poste"
	    verbose_name_plural = "Postes"

	def __str__(self):
	    return '{}'.format(self.titre)

class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Ingredient"
	    verbose_name_plural = "Ingredients"

	def __str__(self):
	    return '{}'.format(self.name)




    
    