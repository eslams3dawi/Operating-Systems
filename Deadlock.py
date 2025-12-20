import threading
import time

resourceOne = threading.Lock()
resourceTwo = threading.Lock()

def threadOne():
    with resourceOne:
        print("acquire for res 1")
        time.sleep(1)
        print("waiting for res 2")
        with resourceTwo:
            print("acquiring res 2 is completed")

def threadTwo():
    with resourceTwo:
        print("acquire for res 2")
        time.sleep(1)
        print("waiting for res 1")
        with resourceOne:
            print("acquiring res 1 is completed")

a = threading.Thread(target=threadOne, name="Thread One")
b = threading.Thread(target=threadTwo, name="Thread Two")

a.start()
b.start()