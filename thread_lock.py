import threading
import time

def count():
    global x, lock
    while x < 1000:
        # critical section
        lock.acquire()
        x = x + 1
        print(f'{x} {threading.currentThread().name} ')
        lock.release()
def getDbConnection():
    global lock
    with lock: # will free automatically when leave the indent
        if connectionAvailable:
            connectionAvailable = False
            conn = "dbConnection"
            return conn
        else:
            return None

lock = threading.Lock()
x = 0
t1 = threading.Thread(target=count)
t1.start()
count()
