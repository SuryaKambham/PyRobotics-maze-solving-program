from pycreate2 import Create2
import time

bot = Create2('/dev/tty.usbserial-DA017VIJ')

bot.start()

bot.safe()

bot.full()

# start your code here
time.sleep(1)

# stepCount equals the number of time moved forward
# (like when you yourself moved forward in the maze, stepCount is like how many times you took a step)
didITurnLeft = False
didITurnRight = False

while True:
    stepCount = 0
    sensor = bot.get_sensors()
    while sensor.light_bumper_center_left < 100 and sensor.light_bumper_center_right < 100:
        bot.drive_direct(100, 110)
        time.sleep(1)
        sensor = bot.get_sensors()
        stepCount += 1
        if stepCount > 2:
            didITurnLeft = False
            didITurnRight = False
        print(stepCount) 

    if didITurnLeft is False:
        bot.drive_rotate(90, 1)
        time.sleep(2)
        bot.drive_stop()
        didITurnLeft = True
    elif didITurnLeft is True and didITurnRight is False:
        bot.drive_rotate(200, 1)
        time.sleep(2)
        bot.drive_stop()
        didITurnRight = True
    else:
        break

bot.stop()
