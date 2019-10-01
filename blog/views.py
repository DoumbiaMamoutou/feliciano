from django.shortcuts import render
from . import models  as art
from configuration import models as config
from django.core.paginator import Paginator 

# Create your views here.

def blog(request):
	paginator =Paginator(art.Article.objects.filter(status=True),6)
	if request.method == 'GET':
		page=request.GET.get('page',1)
	articles = paginator.page(page)
	data = {
		'category':art.Category.objects.filter(status=True),
		'configuration':config.MainConfig.objects.filter(status=True)[:1],
		'working_hour':config.WorkingHour.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True)[:1],
		'articles':articles,

	}
	return render(request, 'pages/blog.html')

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
	return render(request, 'pages/list_date.html')

def list_tag(request,tag):
	return render(request, 'pages/list_tag.html')
def comment(request):
	return ''