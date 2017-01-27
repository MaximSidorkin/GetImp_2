import unittest
from browsermobproxy import Server
from browsermobproxy import Client

from requests.auth import HTTPBasicAuth
from selenium import webdriver
import unittest
import requests
from requests.auth import HTTPDigestAuth


import requests
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
import time
import urllib
import urllib.request as urllib2
import http.cookiejar
from urllib.parse import urlparse

url = 'https://owa.mos.ru/EWS/Exchange.asmx'
login = 'SolovievEV'
password = 'rOURDPTc'

class MyTestCase(unittest.TestCase):
    def test_something_01(self):
        #profile = webdriver.FirefoxProfile()
        #profile.accept_untrusted_certs = True

        server = Server(r"C:\PyTest\browsermob-proxy\bin\browsermob-proxy",  {"port":9090})
        server.start()
        proxy = server.create_proxy()

        profile = webdriver.FirefoxProfile()
        profile.set_proxy(proxy.selenium_proxy())
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(firefox_profile=profile)

        proxy.new_har("owa")
        client = Client("localhost:9090")
        client.basic_authentication(domain='https://owa.mos.ru/EWS/Exchange.asmx',username='SolovievEV',password='rOURDPTc')
        #print(client)

        #owa = driver.get('https://yandex.ru')

        #proxy.har  # returns a HAR JSON blob

        #Client.basic_authentication(self,owa,login,password)

        server.stop()
        driver.quit()

    #def test_something_02(self):
    #    proxys = "localhost:9090"  # в формате прокси:порт
    #    user = 'SolovievEV'  # прокси логин
    #    password = 'rOURDPTc'  # прокси пароль

    #   proxy = urllib2.ProxyHandler({"http": proxys})  # инициализация
    #    proxy_auth_handler = urllib2.ProxyBasicAuthHandler()  # инициализация авторизации в прокси
    #    proxy_auth_handler.add_password('realm', 'uri', user, password)  # добавляем логин и пароль в прокси

    #    cookieJar = http.cookiejar  # инициализация cookielib

    #    opener = urllib2.build_opener(proxy, proxy_auth_handler, urllib2.HTTPCookieProcessor(cookieJar))
    #    urllib2.install_opener(opener)  # устанавливаем загрузчик

    #    params = urllib.parse.urlencode({'name': 'user_login', 'pass': 'user_password', 'submit': 'Войти'})
    #    binary_data = params.encode('bytes') # ('encoding') # (encoding=ascii) # (encoding=bytes)
    #    get = urllib2.Request('https://owa.mos.ru/EWS/Exchange.asmx', binary_data)  # binary_data
    #    f = opener.open(get, params)
    #    f = f.read()  # читаем ответ и выводим в консоль
    #    print(f)

if __name__ == '__main__':
    unittest.main()
