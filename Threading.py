import threading
import time

def printOne():
    print(f"starting of thread 1: {threading.current_thread().name}")
    time.sleep(0.2)
    print(f"finishing of thread 1: {threading.current_thread().name}")

def printTwo():
    print(f"starting of thread 2: {threading.current_thread().name}")
    print(f"finishing of thread 2: {threading.current_thread().name}")

def printThree():
    print(f"starting of thread 3: {threading.current_thread().name}")
    print(f"finishing of thread 3: {threading.current_thread().name}")

a = threading.Thread(target=printOne, name="Thread One")
b = threading.Thread(target=printTwo, name="Thread Two")
c = threading.Thread(target=printThree, name="Thread Three")

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()

print("Main thread: all threads have completed execution")