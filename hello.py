#You can specify a Python version for pip to use:
#pip3.4 install requests
#Python 3.4 has pip support built-in, so you can also use:
#python3.4 -m pip install
#If you're running Ubuntu (or probably Debian as well), you'll need to install the system pip3 separately:
#sudo apt-get install python3-pip
#This will install the pip3 executable, so you can use it, as well as the earlier mentioned python3.4 -m pip:
#pip3 install requests

import time
from requests import get
import datetime;

while True:
    ct = datetime.datetime.now()
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('WAN IP address is: {} - Time '.format(ip))
    print("current time:-", ct)
    time.sleep(5)