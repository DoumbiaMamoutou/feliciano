from django.shortcuts import render
from configuration import models as config
from blog import models as art
from restaurant import models as restau
# Create your views here.
def home(request):
	data = {
		'about':config.AboutConfig.objects.filter(status=True)[:1],
		'service':config.ServiceConfig.objects.filter(status=True),
		'temoin':config.Temoin.objects.filter(status=True),
		'contact':config.ContactConfig.objects.filter(status=True),
		'article_acceuil': art.Article.objects.filter(acceuil=True)[:4],
		'article':art.Article.objects.order_by('-date_add')[:3],
	}
	return render(request, 'pages/index.html',data)

def menu(request):
	cats=restau.Category.objects.filter(status=True)
	data = {
		'category':cats,
	}
	for c in cats :
		data.update({
			c.titre:c.category_plat.all,
		})
	print(data)
	return render(request, 'pages/menu.html',data)

def about(request):
    return render(request, 'pages/about.html')

def reservation(request):
    return render(request, 'pages/reservation.html')

def list_categorie(request):
    return render(request, 'pages/list_categorie.html')

def list_date(request):
    return render(request, 'pages/list_date.html')

def list_tag(request):
    return render(request, 'pages/list_tag.html')