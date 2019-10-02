from django.shortcuts import render,redirect
from . import models  as art
from .models import *
from configuration import models as config
from django.core.paginator import Paginator 
from . import forms
# Create your views here.

def blog(request):
    
	# paginator =Paginator(art.Article.objects.filter(status==True),6)
	# if request.method == 'GET':
	# 	page=request.GET.get('page',1)
	# articles = paginator.page(page)
	lister = Article.objects.filter(status=True)
	data = {
		# 'category':art.Category.objects.filter(status=True),
		# 'configuration':config.MainConfig.objects.filter(status=True)[:1],
		# 'working_hour':config.WorkingHour.objects.filter(status=True),
		# 'instagram':config.Instagram.objects.filter(status=True)[:1],
		# 'articles':articles,
		'lister':lister,

	}
	return render(request, 'pages/blog.html',data)

def single(request,id):
	data={
		'configuration':config.MainConfig.objects.filter(status=True)[:1],
		'working_hour':config.WorkingHour.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True)[:1],
		'category':art.Category.objects.filter(status=True),
		'article':art.Article.objects.get(pk=id),
		'art_popu':art.Article.objects.select_related('comment').order_by('comment__count'),
		'tags':art.Tags.objects.filter(status=True),
	}

	return render(request,'pages/single.html')

def list_categorie(request,category):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if q:
			articles = art.Article.objects.filter(titre__contains=q).filter(category=category)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
		else:
			articles = art.Articles.objects.filter(category=category)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
	return render('blog')

def list_date(request,date):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if q:
			articles = art.Article.objects.filter(titre__contains=q).filter(date_add=date)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
		else:
			articles = art.Articles.objects.filter(date_add=date)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
	return redirect('blog')

def list_tag(request,tag):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('p',1)
		if q:
			articles = art.Article.objects.filter(titre__contains=q).filter(tag__contains=tag)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
		else:
			articles = art.Articles.objects.filter(tag__contains=tag)
			art =Paginator(articles,10)
			art = paginator.page(p)
			return render(request, 'pages/list_categorie.html',art)
	return redirect('blog')
def comment(request):
	if request.method == 'POST':
		comment = forms.CommentForm(request.POST)
		if comment.is_valid:
			comment.save()
	return redirect('blog')