import urllib.request
import threading
import time

#urllib.request.urlretrieve('http://www.study-io.com/java/installations/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi','c:/itay/1.msi')
url = 'https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/152964589-welcome-home-new-cat-632x475.jpg'
#filename = ?
urllib.request.urlretrieve(url, f'c:/itay/{filename}')
