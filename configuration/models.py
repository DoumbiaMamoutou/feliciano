from django.db import models
from tinymce import HTMLField
from django.utils.timezone import now
from datetime import datetime, date, time
import re
# Create your models here.

class MainConfig(models.Model):
	# TODO: Define fields here
	nom = models.CharField(max_length=50)
	description = models.TextField()
	working_hour = models.ManyToManyField('WorkingHour',related_name='working_config')
	instagram = models.ForeignKey('Instagram',on_delete=models.CASCADE,related_name='insta_config')
	text1 = models.CharField(max_length=50)
	text2 = models.CharField(max_length=50)
	text3 = models.CharField(max_length=50)
	image1 = models.ImageField(upload_to='home/')
	image2 = models.ImageField(upload_to='home/')
	image3 = models.ImageField(upload_to='home/')
	scroll_image = models.ImageField(upload_to='home/')
	tel = models.CharField(max_length=15)
	email = models.EmailField(max_length=255)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	social = models.ManyToManyField('Social',related_name='social_config')
	@property
	def open_hour(self):
		jour = now().strftime('%A')
		hour = ''
		for w in self.working_hour:
			if re.match(w.jour,jour,re.IGNORECASE):
				hour = '{} - {}'.format(w.start_hour,w.end_hour)
		print(jour,' : ',hour)
		return '{} : {}'.format(jour,hour)

	class Meta:
	    verbose_name = "MainConfig"
	    verbose_name_plural = "MainConfigs"

	def __str__(self):
	    return '{}'.format(self.nom)

class Day(models.Model):
	# TODO: Define fields here
	jour = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = "Day"
		verbose_name_plural = "Days"

	def __str__(self):
		return '{}'.format(self.jour)


class WorkingHour(models.Model):
	# TODO: Define fields here
	jour = models.ForeignKey(Day,on_delete=models.CASCADE,related_name='day_working')
	start_hour = models.CharField(max_length=50)
	end_hour = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "WorkingHour"
	    verbose_name_plural = "WorkingHours"

	def __str__(self):
	    return '{}  {} - {}'.format(self.jour,self.start_hour,self.end_hour)


class Instagram(models.Model):
	# TODO: Define fields here
	image1 = models.ImageField(upload_to='home/insta')
	image2 = models.ImageField(upload_to='home/insta')
	image3 = models.ImageField(upload_to='home/insta')
	image4 = models.ImageField(upload_to='home/insta')
	image5 = models.ImageField(upload_to='home/insta')
	image6 = models.ImageField(upload_to='home/insta')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)


	class Meta:
	    verbose_name = "Instagram"
	    verbose_name_plural = "Instagrams"



class Social(models.Model):
	# TODO: Define fields here
	choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
	name = models.CharField(max_length=100,choices=choice)
	lien = models.URLField(max_length=200)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)


	@property
	def font(self):
		if self.name == 'facebook':
			font = 'icon-facebook'
		elif self.name == 'tiwtter':
			font ='icon-twitter'
		elif self.name == 'instagram':
			font ='icon-instagram"'
		elif self.name == 'google':
			font ='icon-google-plus'

	class Meta:
	    verbose_name = "Social"
	    verbose_name_plural = "Socials"

	def __str__(self):
	    return '{}'.format(self.name)

class Icon(models.Model):
	# TODO: Define fields here
	name = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)


	class Meta:
	    verbose_name = "Icon"
	    verbose_name_plural = "Icons"

	def __str__(self):
	    return '{}'.format(self.name)


class AboutConfig(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	content = HTMLField('content')
	open_hour = models.CharField(max_length=255)
	phone = models.CharField(max_length=50)
	yoe = models.IntegerField()
	menu = models.IntegerField()
	satff = models.IntegerField()
	happy_customer = models.IntegerField()
	description = models.TextField()
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "AboutConfig"
	    verbose_name_plural = "AboutConfigs"

	def __str__(self):
	    return '{}'.format(self.titre)


    
class ServiceConfig(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	description = models.TextField()
	icone = models.ForeignKey(Icon,on_delete=models.CASCADE,related_name='icon_service')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "ServiceConfig"
	    verbose_name_plural = "ServiceConfigs"

	def __str__(self):
	    return '{}'.format(self.titre)



class Temoin(models.Model):
	# TODO: Define fields here
	name = models.CharField(max_length=50)
	job = models.CharField(max_length=50)
	comment = models.TextField()
	image = models.ImageField(upload_to='testimonial')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "Temoin"
	    verbose_name_plural = "Temoins"

	def __str__(self):
	    return '{}'.format(self.name)


class ContactConfig(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	image = models.ImageField(upload_to='home/contact')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "ContactConfig"
	    verbose_name_plural = "ContactConfigs"

	def __str__(self):
	    return self.titre


class BlogConfig(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	image = models.ImageField(upload_to='home/contact')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "BlogConfig"
	    verbose_name_plural = "BlogConfigs"

	def __str__(self):
	    return self.titre


class MenuConfig(models.Model):
	# TODO: Define fields here
	titre = models.CharField(max_length=50)
	image = models.ImageField(upload_to='home/contact')
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	class Meta:
	    verbose_name = "MenuConfig"
	    verbose_name_plural = "MenuConfigs"

	def __str__(self):
	    return self.titre


