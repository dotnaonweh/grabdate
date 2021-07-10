import requests
import re

date = input("Date > ")

for page in range(1,100):

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = requests.get('https://www.cubdomain.com/domains-registered-by-date/'+date+'/'+str(page), headers=headers).content.decode('utf-8')
    rex = re.findall('<a href="(.*?)">', req)

    for i in rex:
        if 'https://www.cubdomain.com/site/' in rex:
            pass
        elif 'tools' in i:
            pass
        elif 'domains' in i:
            pass
        elif 'javascript:;"' in i:
            pass
        elif 'dcounter.cubdom' in i:
            pass
        elif 'contact"' in i:
            pass 
        elif 'about"' in i:
            pass
        elif 'chrome.goo' in i:
            pass  
        elif 'er.com/inte' in i:
            pass
        elif 'facebook.com/cubdo' in i:
            pass
        elif 'rest.com/cub' in i:
            pass
        elif 'domain.com"' in i:
            pass
        elif 'domain.com/privacy-' in i:
            pass
        elif 'ain.com/terms-and' in i:
            pass
        elif 'in.com/cookies-po' in i:
            pass
        elif 'ain.com/disclaimer"' in i:
            pass
        elif 'in.com/l/interserver"' in i:
            pass
        else:
            rp = i.replace("https://www.cubdomain.com/site/","")
            print("Grab > ", rp)
            result = open('result.txt', 'a').write(str(rp)+'\n')