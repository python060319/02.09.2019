import threading
import time

def sleeper():
    print(threading.currentThread().name)
    print("start")
    time.sleep(4)
    print('end')

#t1 = threading.Thread(target=sleeper
#      ,name="my Thread")
#print(t1.name)

#print(threading.currentThread().name)
#t1.daemon = True # Background
#t1.start() # new thread call sleeper
#sleeper() # main call sleeper
#print("\nmain has left the building...")
# cannot go home...

def countDown(number):
    while True:
        number = number - 1
        print(number)
        time.sleep(1)
        if number == 0:
            break

t1 = threading.Thread(target=countDown
                      , args=(5,))
t1.start()
x = input("\n5 * 12 = ?")
if t1.isAlive():
    print("On time!")
else:
    print("TimeOut!")
