from . import models as config

def get_config(request):
	data={
		'configuration':config.MainConfig.objects.filter(status=True)[:1],
		'working_hour':config.WorkingHour.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True)[:1],
		'about':config.AboutConfig.objects.filter(status=True)[:1],
		'service':config.ServiceConfig.objects.filter(status=True),
		'temoin':config.Temoin.objects.filter(status=True),
	}
	return data