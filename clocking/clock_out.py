from datetime import datetime
import os

DAILY_CLOCK_IN = "logs/daily_clock_in.txt" # Stores time in which user clocked in
HOURS_LOG = "logs/hours_log.txt" # stores hours over weeks in which user clocked in

def clock_out(dummy):
    os.system("clear")
    clock_in_value = open(DAILY_CLOCK_IN, "r+")
    
    clock_in_time = clock_in_value.read()
    clock_in_time = datetime.strptime(clock_in_time, "%Y-%m-%d %H:%M:%S.%f")
    
    clock_out_time = datetime.now()
    date, time = str(clock_out_time).split(" ")

    time = time.split(".")[0]
    time = datetime.strptime(time, "%H:%M:%S")
    time = time.strftime("%I:%M:%S %p")

    time_worked = clock_out_time - clock_in_time
    time_worked = str(time_worked)
    time_worked = time_worked.split('.')[0]

    save_log = open(HOURS_LOG, "a+")
    save_log.write(date + " " + time_worked + "\n")

    print("Successfully clock out, here's a log")
    print("Date: " + date)
    print("Time: " + time)
    print("Time Worked: " + time_worked)

    clock_in_value.close()
    save_log.close()    

if __name__ == '__main__':
    clock_out("TEST MODE")