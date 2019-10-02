import requests
import json
from . import models
def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    url = "https://ipapi.com/ip_api.php?ip={}"
    try:
        req = requests.get(url.format(ip))
        if req.status_code:
            data = json.loads(req.text)
            latitude = data['latitude']
            longitude = data['longitude']
            pays = data['country_name']
            ville = data['city']
            continent = data['continent_name']
            reseau = data['connection']['isp']
            client = models.Client(
                ip=ip,
                pays=pays,
                ville=ville,
                continent=continent,
                reseau=reseau,
                latitude=latitude,
                longitude=longitude
            )
            client.save()
    except :
        print('error')
    return {'ip':ip}


