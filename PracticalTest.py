# import threading
# import time

# def thread1():
#     print("Starting of thread 1")
#     time.sleep(1)
#     print("Ending of thread 1")

# def thread2():
#     print("Starting of thread 2")
#     print("Ending of thread 2")

# a = threading.Thread(target=thread1, name="Thread One")
# b = threading.Thread(target=thread2, name="Thread Two")

# a.start()
# b.start()

# a.join()
# b.join()

#2
# import threading
# import time

# def patientTask(patientId):
#     print(f"Patient {patientId}, started the treatment")
#     time.sleep(10)
#     print(f"Patient {patientId}, finished his treatment")

# def managePatients(Patients, UserCount):

#     for i in range(UserCount):
#         patient = threading.Thread(target=patientTask, args=(i, ), name=f"Thread {i+1}")
#         Patients.append(patient)
#         patient.start()

# UserCount = int(input("Enter number of patients: "))
# Patients = []
# managePatients(Patients, UserCount)
# for patient in Patients:
#     patient.join()

# print("Main: all threads have been completed")


#6
import threading
import time

resource1 = threading.Lock()
resource2 = threading.Lock()

def thread1():
    with resource1:
        print(f"Thread 1 acquire res 1")
        time.sleep(3)
        print(f"Thread 1 waiting for res 2")
        with resource2:
            print(f"Thread 1 acquire res 2 completed")

def thread2():
    with resource2:
        print(f"Thread 2 acquire res 2")
        time.sleep(5)
        print(f"Thread 2 waiting for res 1")
        with resource1:
            print(f"Thread 2 acquire res 1 completed")

a = threading.Thread(target=thread1, name="Thread one")
b = threading.Thread(target=thread2, name="Thread two")

a.start()
b.start()

a.join()
b.join()