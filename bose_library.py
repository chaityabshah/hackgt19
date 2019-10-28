import requests
import xmltodict

def get_bass():
    url = 'http://192.168.1.174:8090/bass'
    x = requests.get(url)
    return int(xmltodict.parse(x.text, dict_constructor=dict)["bass"]["actualbass"])

def get_volume():
    url = 'http://192.168.1.174:8090/volume'
    x = requests.get(url)
    return int(xmltodict.parse(x.text, dict_constructor=dict)["volume"]["actualvolume"])

def set_bass(bass):
    url = 'http://192.168.1.174:8090/bass'
    x = requests.post(url, '<bass>' + str(bass) + '</bass>')

def set_volume(vol):
    url = 'http://192.168.1.174:8090/volume'
    x = requests.post(url, '<volume>' + str(vol) + '</volume>')
