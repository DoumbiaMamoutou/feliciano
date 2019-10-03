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
		'article_acceuil': restau.Plat.objects.filter(status=True)[:4],
		'plat':restau.Plat.objects.filter(status=True).order_by('prix')[:6],
		'chef':restau.Chef.objects.filter(status=True)[:4],
		'article':art.Article.objects.order_by('-article_comment')[:3],
	}
	return render(request, 'pages/index.html',data)

def menu(request):
	p = request.GET.get('page',1)
	cat = request.GET.get('category',False)
	cats=restau.Category.objects.filter(status=True)
	data = {}
	values = {}
	for c in cats :
		values.update({
			c.titre:c.category_plat.all().order_by('id'),
		})
	for k,d in values.items() :
		if cat == k and len(d) is not None:
			paginator=Paginator(d,6)
			d = paginator.page(p)
		elif cat == False and len(d) is not None:
			paginator=Paginator(d,6)
			d = paginator.page(p)
	data.update({'category':cats,'values':values})
	return render(request, 'pages/menu.html',data)

def about(request):
	data = {
		'about':config.AboutConfig.objects.filter(status=True)[:1].get(),
		'service':config.ServiceConfig.objects.filter(status=True),
		'temoin':config.Temoin.objects.filter(status=True),
		'chef':restau.Chef.objects.filter(status=True)[:4],
	}
	print(data['chef'])
	return render(request, 'pages/about.html',data)


