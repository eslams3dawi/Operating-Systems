import schedule
import time

def alarm():
    print("Wake up!!")

schedule.every(5).seconds.do(alarm)

while True:
    schedule.run_pending()
    time.sleep(1)
