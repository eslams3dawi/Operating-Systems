import threading
import time

# Three resources
res1 = threading.Lock()
res2 = threading.Lock()
res3 = threading.Lock()

def threadOne():
    with res1:
        print("Thread 1 acquired Resource 1")
        time.sleep(1)
        print("Thread 1 waiting for Resource 2")
        with res2:
            print("Thread 1 acquired Resource 2")

def threadTwo():
    with res2:
        print("Thread 2 acquired Resource 2")
        time.sleep(1)
        print("Thread 2 waiting for Resource 3")
        with res3:
            print("Thread 2 acquired Resource 3")

def threadThree():
    with res3:
        print("Thread 3 acquired Resource 3")
        time.sleep(1)
        print("Thread 3 waiting for Resource 1")
        with res1:
            print("Thread 3 acquired Resource 1")

t1 = threading.Thread(target=threadOne)
t2 = threading.Thread(target=threadTwo)
t3 = threading.Thread(target=threadThree)

t1.start()
t2.start()
t3.start()
