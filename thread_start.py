import threading
import time

def sleeper():
    print("start")
    time.sleep(4)
    print('end')

t1 = threading.Thread(target=sleeper)
t1.daemon = False # Background
t1.start() # new thread call sleeper
#sleeper() # main call sleeper
print("\nmain has left the building...")
#t1.join()
# cannot go home...