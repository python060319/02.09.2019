import urllib.request
import threading
import time
import os

url = 'https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/152964589-welcome-home-new-cat-632x475.jpg'
filename = os.path.basename(url)
urllib.request.urlretrieve(url, f'c:/itay/{filename}')

# one thread dlownload thi huge file
# 'http://www.study-io.com/java/installations/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi'
# second thread counts the seconds...
# when download completed counting thread will finish
# *etgar: show percentage
# urlopen -> info - content-length
# os - what is thc urrent file size
# 100 * current / total = %

d = urllib.request.urlopen('http://www.study-io.com/java/installations/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi')
print(d.info().get('content-length'))
