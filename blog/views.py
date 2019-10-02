import os
from django.conf import settings
from django.shortcuts import render,redirect
from .models import *
from random import randint
from django_seed import Seed
from configuration import models as config
from django.core.paginator import Paginator 
from . import forms
from faker import Faker
# Create your views here.
def blog(request):

	paginator =Paginator(Article.objects.filter(status=True),6)
	if request.method == 'GET':
		page=request.GET.get('page',1)
	articles = paginator.page(page)
	data = {
		'category':Category.objects.filter(status=True),
		'configuration':config.MainConfig.objects.filter(status=True)[:1],
		'working_hour':config.WorkingHour.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True)[:1],
		'articles':articles,

	}
	
	return render(request, 'pages/blog.html',data)

def single(request,id):
	data={
		'configuration':config.MainConfig.objects.filter(status=True)[:1],
		'working_hour':config.WorkingHour.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True)[:1],
		'category':Category.objects.filter(status=True),
		'article':Article.objects.get(pk=id),
		'art_popu':Article.objects.select_related('comment').order_by('comment__count'),
		'tags':Tag.objects.filter(status=True),
	}

	return render(request,'pages/single.html',data)

def list_categorie(request,category):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(category=category)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
		else:
			articles = Article.objects.filter(category=category)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
	return redirect('blog')

def list_date(request,date):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(date_add=date)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
		else:
			articles = Article.objects.filter(date_add=date)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
	return redirect('blog')

def list_tag(request,tag):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(tag__contains=tag)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
		else:
			articles = Article.objects.filter(tag__contains=tag)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			return render(request, 'pages/list_categorie.html',arti)
	return redirect('blog')
def comment(request):
	if request.method == 'POST':
		comment = forms.CommentForm(request.POST)
		if comment.is_valid:
			comment.save()
	return redirect('blog')
def artFake(request):
	from django.core.files import File
	fake = Faker()
	category = Category.objects.filter(status=True)
	tag=Tag.objects.filter(status=True)
	auteur = Author.objects.get(pk=2)
	images = {
		'Breakfast':[os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)],
		'Lunch':[os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)],
		'Dinner':[os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)],
		'desserts':[os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)],
		'drinks':[os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)],
	}
	inter =0
	while inter < 100:
		imgs=[]
		cat = category[randint(0,5)]
		for k,v in images.items():
			if k == cat.titre:
				imgs=v
		inter += 1
		art = Article(
			titre=fake.sentence(nb_words=15, variable_nb_words=True, ext_word_list=None),
			description= fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
			contenu=fake.text(max_nb_chars=800, ext_word_list=None),
			category= cat,
			author=auteur,
			acceuil= fake.boolean(),
		)
		img=imgs[randint(0,len(imgs)-1)]
		img = open(img,'rb')
		name='{}.jpg'.format(cat.titre)
		print('====================\r\n',img,'\r\n=========================\r\n',img.name,'\r\n=======================\r\n')
		art.image.save(name, File(img))
		for t in tag:
			art.tag.add(t)
		art.save()
	return redirect('blog')

def comFake(request):
	from django.core.files import File
	fake = Faker()
	article = Article.objects.filter(status=True)
	images = [os.path.join(settings.BASE_DIR,'static/images/person_'+str(i)+'.jpg') for i in range(1,5)]
	inter =0
	while inter < 100:
		art = article[randint(0,310)]
		inter += 1
		nom=fake.name()
		comment =Comment(
			article=art,
			message= fake.paragraph(nb_sentences=2, variable_nb_sentences=True, ext_word_list=None),
			name= nom,
			email=fake.safe_email(),
			website=fake.uri(),
		)
		img=images[randint(0,len(images)-1)]
		img = open(img,'rb')
		name='{}.jpg'.format(nom)
		print('====================\r\n',img,'\r\n=========================\r\n',img.name,'\r\n=======================\r\n')
		comment.image.save(name, File(img))
		img.close()
	return redirect('blog')


# def delete(request):
# 	art = Article.objects.filter(status=True)
# 	art.delete()
# 	return redirect('blog')