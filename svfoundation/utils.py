import requests
from countryinfo import CountryInfo


def get_country_by_ip(ip: str):
    return get_country_with_ip_api(ip)


def get_country_with_ip_api(ip: str):
    res = requests.get(f'http://ip-api.com/json/{ip}?fields=status,countryCode')
    data = res.json()
    if data.get('status') == 'success':
        return data.get('countryCode')


def get_country_currencies(country_code):
    try:
        return CountryInfo(country_code).currencies()
    except KeyError:
        return []


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
