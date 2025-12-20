import threading
import time

hr = threading.Semaphore(2)

def EnterInterviewRoom(num):
	print(f"Employee {num} is waiting for his turn")
	
	hr.acquire()
	print(f"Employee {num} is in the room")
	time.sleep(10)

	print(f"Employee {num} leaves the room")
	hr.release()

count = int(input("Enter the count"))

Employees = []
for i in range(count):
	employee = threading.Thread(target=EnterInterviewRoom, args=(i,))
	Employees.append(employee)
	employee.start()

for employee in Employees:
	employee.join()


	