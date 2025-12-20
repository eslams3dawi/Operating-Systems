import threading
import time

hr = threading.Semaphore(1)

def EnterInterview(num):
   print(f"employee {num} is waiting for his turn")

   hr.acquire()
   print(f"employee {num} is in the interveiw room")
   time.sleep(5)

   print(f"employee {num} is leaves the interview room")
   hr.release()

countOfEmployees = int(input("Enter the count"))
Employees = []
for i in range(countOfEmployees):
   employee = threading.Thread(target=EnterInterview, args=(i,))
   Employees.append(employee)
   employee.start()

for employee in Employees:
   employee.join()