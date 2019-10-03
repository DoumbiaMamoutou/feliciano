import os
from django.conf import settings
from django.shortcuts import render,redirect
from .models import *
from random import randint
# from django.seed import Seed
from configuration import models as config
from django.core.paginator import Paginator 
from . import forms
from faker import Faker
# Create your views here.
def blog(request):

	if request.method == 'GET':
		page=request.GET.get('page',1)
		paginator =Paginator(Article.objects.filter(status=True).order_by('article_comment'),6)
		articles = paginator.page(page)
		data = {
			'category':Category.objects.filter(status=True),
			'configuration':config.MainConfig.objects.filter(status=True)[:1],
			'working_hour':config.WorkingHour.objects.filter(status=True),
			'instagram':config.Instagram.objects.filter(status=True)[:1],
			'articles':articles,

		}
		return render(request, 'pages/blog.html',data)
	return redirect('blog')

def single(request,id):
	data={
		'category':Category.objects.filter(status=True),
		'article':Article.objects.get(pk=id),
		'art_popu':Article.objects.filter(status=True).order_by('-article_comment')[:4],
		'art_date':Article.objects.filter(status=True).order_by('-date_add')[:6],
		'tags':Tag.objects.filter(status=True),
	}
	print('==============================\r\n',data['art_date'],'\r\n===================================')

	return render(request,'pages/single.html',data)

def list_categorie(request,category):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('page',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(category=category)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data={
				'articles':arti,
				'category':Category.objects.get(pk=category)
			}
			return render(request, 'pages/list_categorie.html',data)
		else:
			articles = Article.objects.filter(category=category)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data={
				'articles':arti,
				'category':Category.objects.get(pk=category)
			}
			return render(request, 'pages/list_categorie.html',data)
	return redirect('blog')

def list_date(request,date):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('page',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(date_add=date)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data = {
				'articles':arti,
				'date':date
			}
			return render(request, 'pages/list_date.html',data)
		else:
			articles = Article.objects.filter(date_add=date)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data = {
				'articles':arti,
				'date':date
			}
			return render(request, 'pages/list_date.html',data)
	return redirect('blog')

def list_tag(request,tag):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('page',1)
		if query:
			articles = Article.objects.filter(titre__contains=query).filter(tag=tag)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data = {
				'articles':arti,
				'tag':Tag.objects.get(pk=tag)
			}
			return render(request, 'pages/list_tag.html',data)
		else:
			articles = Article.objects.filter(tag=tag)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data = {
				'articles':arti,
				'tag':Tag.objects.get(pk=tag)
			}
			return render(request, 'pages/list_tagx.html',data)
	return redirect('blog')
def comment(request):
	if request.method == 'POST':
		comment = forms.CommentForm(request.POST)
		if comment.is_valid:
			comment.save()
	return redirect('blog')

def blogSearch(request):
	if request.method == 'GET':
		query=request.GET.get('q',False)
		p = request.GET.get('page',1)
		if query:
			articles = Article.objects.filter(titre__contains=query)
			arti =Paginator(articles,10)
			arti = arti.page(p)
			data={
				'articles':arti,
			}
			return render(request, 'pages/list.html',data)
	return redirect('blog')