import datetime
import time
import winsound  # For Windows systems, you can use the winsound module for sound notifications

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            # Play a sound notification (Windows only)
            winsound.Beep(1000, 1000)  # 1000 Hz sound for 1 second
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock App")
    print("Please enter the time for your alarm (HH:MM:SS format):")

    while True:
        try:
            alarm_time = input("Set the alarm: ")
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")

    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
