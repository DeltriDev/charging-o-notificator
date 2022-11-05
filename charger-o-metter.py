import os
import time

try:
    import psutil
except ImportError:
    input(f"Module pynput not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install psutil'\nPress enter to exit")
    exit()

try:
    import plyer
except ImportError:
    input(f"Module pynput not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install plyer'\nPress enter to exit")
    exit()
from plyer import notification

# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
# returns a tuple
battery = psutil.sensors_battery()
  
print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)
  
# converting seconds to hh:mm:ss
print("Battery left : ", convertTime(battery.secsleft))

while(True):
    if battery.power_plugged == True:
        notification.notify(
            title = "Your laptop charging review",
            message = "Charging battery percentage : {batterypercent}".format(
                batterypercent = battery.percent
            ),
            app_icon = "battery.ico",
            timeout = 10
        )
    else:
        notification.notify(
            title = "Your laptop battery review",
            message = "Battery percentage : {batterypercent}\nScreen time left: {screentime}".format(
                batterypercent = battery.percent,
                screentime = convertTime(battery.secsleft)
            ) ,
            app_icon = "battery.ico",
            timeout = 10
        )
    print("Now waiting 10 minutes")
    time.sleep(60*10)