#You can specify a Python version for pip to use:
#pip3.4 install requests
#Python 3.4 has pip support built-in, so you can also use:
#python3.4 -m pip install
#If you're running Ubuntu (or probably Debian as well), you'll need to install the system pip3 separately:
#sudo apt-get install python3-pip
#This will install the pip3 executable, so you can use it, as well as the earlier mentioned python3.4 -m pip:
#pip3 install requests

import time
import requests
from requests import get
import datetime;

while True:
    ct = datetime.datetime.now()
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('WAN IP address is: ', ip)
    print("Time: ", ct)

    r = requests.post('http://helium.berkay.click/ip/' + ip + '/time/' + str(ct))
    print(r.url)
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')
    time.sleep(60)