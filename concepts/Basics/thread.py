import threading
import time

def wait():
    time.sleep(3)
    print("HEllo")
    
t=threading.Thread(target=wait,args=())
t.start()
print(threading.active_count())