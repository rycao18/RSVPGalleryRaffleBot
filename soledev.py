import requests
from random import randint
from threading import Thread


tasks = int(input('Enter number of tasks:'))

s = requests.Session()

fullname = 'John Smith'
email = 'JohnSmith@gmail.com'
shoesize = '10'


try:
    t = email.split('@')
except:
    print('Invalid email.')
    exit()

def raffle(x, email):
    prefix = email.split('@')[0]
    domain = email.split('@')[1]
    longnum = randint(10000,1000000)
    email = prefix + str(longnum) + '@' + domain


    raffleurl = 'https://rsvpgallery.us1.list-manage.com/subscribe/post-json?u=3c5152418ea66cfe94686365b&id=1e7263dae2&c=jQuery32105118816531413464_1516058119053&FULLNAME={}&EMAIL={}&SHOESIZE={}&_=1516058119054'.format(fullname, email, shoesize)



    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'_AVESTA_ENVIRONMENT=prod',
    'Host':'rsvpgallery.us1.list-manage.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    z = s.get(raffleurl, headers=headers)
    if 'Almost finished... We need to confirm your email address' in z.text:
        print('[Task %s]: Successful registration, confirm email address.' %x)


for x in range(0, tasks):
    t = Thread(target=raffle, args=(x,email))
    t.start()