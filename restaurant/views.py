from django.shortcuts import render
from configuration import models as config
from blog import models as art
from restaurant import models as restau
from django.core.paginator import Paginator 
# Create your views here.
def home(request):
	data = {
		'about':config.AboutConfig.objects.filter(status=True)[:1],
		'service':config.ServiceConfig.objects.filter(status=True),
		'temoin':config.Temoin.objects.filter(status=True),
		'contact':config.ContactConfig.objects.filter(status=True),
		'article_acceuil': art.Article.objects.filter(acceuil=True)[:4],
		'chef':restau.Chef.objects.filter(status=True)[:4],
		'article':art.Article.objects.order_by('-date_add')[:3],
	}
	return render(request, 'pages/index.html',data)

def menu(request):
	p = request.GET.get('page',1)
	cat = request.GET.get('category',False)
	cats=restau.Category.objects.filter(status=True)
	data = {}
	for c in cats :
		data.update({
			c.titre:c.category_plat.all(),
		})
	for k,d in data.items() :
		if cat == k and len(d) is not None:
			paginator=Paginator(d,6)
			d = paginator.page(p)
		elif cat == False and len(d) is not None:
			paginator=Paginator(d,6)
			d = paginator.page(p)
	print(data)
	data.update({'category':cats,})
	return render(request, 'pages/menu.html',data)

def about(request):
	data = {
		'about':config.AboutConfig.objects.filter(status=True)[:1],
		'service':config.ServiceConfig.objects.filter(status=True),
		'temoin':config.Temoin.objects.filter(status=True),
		'chef':restau.Chef.objects.filter(status=True)[:4],
	}
	return render(request, 'pages/about.html')

def reservation(request):
    return render(request, 'pages/reservation.html')

def list_categorie(request):
    return render(request, 'pages/list_categorie.html')

def list_date(request):
    return render(request, 'pages/list_date.html')

def list_tag(request):
    return render(request, 'pages/list_tag.html')