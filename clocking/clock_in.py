from datetime import datetime
import os

DAILY_CLOCK_IN = "logs/daily_clock_in.txt" # Stores time in which user clocked in

def clock_in(dummy):
    os.system("clear")

    clock_in_storage = open(DAILY_CLOCK_IN, "w+")

    clock_in_time = str(datetime.now())
    clock_in_storage.write(clock_in_time)

    clock_in_storage.close()

    date, time = clock_in_time.split(" ")
    time = time.split(".")[0]
    time = datetime.strptime(time, "%H:%M:%S")
    time = time.strftime("%I:%M:%S %p")

    print("Successfully recorded clock in")
    print("Date: " + date)
    print("Time: " + time)
        
if __name__ == "__main__":
    clock_in("TEST MODE") # included in case of future debugging
