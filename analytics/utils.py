import json
import urllib.request

from django.urls import resolve

from .models import ClientConnection, UserClientConnection


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class IPInfo:
    def __init__(self, ip):
        self.url = "https://freegeoip.app/json/"
        self.ip = ip

    def ip_request(self, key):
        try:
            req = urllib.request.Request("{}{}".format(self.url, self.ip))
        except Exception as err:
            print(f'Error occurred: {err}')
            return "missing"
        else:
            try:
                with urllib.request.urlopen(req) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    print(data)
                    if data[key]:
                        return data[key]
                    else:
                        return "missing"
            except Exception as err:
                return "missing"

    def country_code(self):
        return self.ip_request("country_code")

    def country_name(self):
        return self.ip_request("country_name")

    def region_code(self):
        return self.ip_request("region_code")

    def region_name(self):
        return self.ip_request("region_name")

    def city(self):
        return self.ip_request("city")

    def zip_code(self):
        return self.ip_request("zip_code")

    def latitude(self):
        return self.ip_request("latitude")

    def longitude(self):
        return self.ip_request("longitude")

    def metro_code(self):
        return self.ip_request("metro_code")


def page_view(r):
    # Analytics
    info = IPInfo(get_client_ip(r))
    if r.user.is_authenticated:
        new_connection = UserClientConnection(
                                            ip=get_client_ip(r),
                                            user=r.user,
                                            url=str(r.META.get('HTTP_HOST')),
                                            request_body=str(r.META),
                                            country_code=info.country_code(),
                                            country_name=info.country_name(),
                                            region_code=info.region_code(),
                                            region_name=info.region_name(),
                                            city=info.city(),
                                            zip_code=info.zip_code(),
                                            latitude=info.latitude(),
                                            longitude=info.longitude(),
                                            metro_code=info.metro_code(),)
        new_connection.save()
        
    else:
        new_connection = ClientConnection(
                                        ip=get_client_ip(r),
                                        url=str(r.META.get('HTTP_HOST')),
                                        request_body=str(r.META),
                                        country_code=info.country_code(),
                                        country_name=info.country_name(),
                                        region_code=info.region_code(),
                                        region_name=info.region_name(),
                                        city=info.city(),
                                        zip_code=info.zip_code(),
                                        latitude=info.latitude(),
                                        longitude=info.longitude(),
                                        metro_code=info.metro_code(),)
        new_connection.save()

    for arg in args:
        obj = UserClientConnection.objects.get(pk=new_connection.id)
        obj.url = str(r.META.get('HTTP_HOST')) + '/' + str(arg) + '/'
        obj.save()

    for arg in args:
        obj = ClientConnection.objects.get(pk=new_connection.id)
        obj.url = str(r.META.get('HTTP_HOST')) + '/' + str(arg) + '/'
        obj.save()
