## **Introduction**

It is recommended to use the [micro:bit Python Editor](https://python.microbit.org/v/3) when working through these tutorials.

In this tutorial we will refer to our :MOVE Motor robot as a buggy by storing it in a variable called **buggy**.

Make sure that your :MOVE Motor chassis is switched on when you want to run a program. You should press the micro:bit's power button to restart the stored program.

## **Moving the :MOVE Motor forward**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

buggy.motorOn("l", "f", 25) # (1)!
buggy.motorOn("r", "f", 25)
```

1. `motorOn()` accepts three arguments (motor, direction, speed).

To stop the buggy moving we will need to switch off the chassis because we never turn the motors off in the program.

## **Moving the :MOVE Motor backward**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

buggy.motorOn("l", "r", 25)
buggy.motorOn("r", "r", 25)
```

We can move the buggy backward by changing the second argument for both calls to `motorOn()` to `"r"` for reverse.

## **Moving the :MOVE Motor forward, stopping after 5 seconds**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

buggy.motorOn("l", "f", 25)
buggy.motorOn("r", "f", 25)
sleep(5000)
buggy.stopMotors() # (1)!
```

1. `stopMotors()` will stop both the left and right motors.

`sleep(5000)` will suspend the execution of the program for 5 seconds (5000ms).

## **Turning on one wheel**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

buggy.motorOn("l", "f", 25)
buggy.motorOn("r", "f", 25)
sleep(2000)
buggy.stopMotors()
buggy.motorOn("l", "f", 25)
sleep(1000)
buggy.motorOff("l")
```

The program above starts off by moving forward for 2 seconds then turns right by only powering the left motor and keeping the right motor off.

## **Turning by pivoting**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

buggy.motorOn("l", "f", 25)
buggy.motorOn("r", "f", 25)
sleep(2000)
buggy.stopMotors()
buggy.motorOn("l", "f", 25)
buggy.motorOn("r", "r", 25)
sleep(500)
buggy.stopMotors()
```

The program above will cause the robot to turn on the spot as one motor is put in reverse while the other remains forward.

## **Using the ultrasonic sensor**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

while True: # (1)!
    distance = buggy.measureDistance() # (2)!
    if distance > 10:
        buggy.motorOn("l", "f", 25)
        buggy.motorOn("r", "f", 25)
    else:
        buggy.stopMotors()
```

1. We need to use a loop so it keeps checking the distance.
2. The distance returned is in centimetres

The program below will move forward at the speed of 25 if there isn't an object within a 10cm range front of it.

## **Using the line following sensor**

``` py linenums="1" title="main.py"
from microbit import *
from KitronikMOVEMotor import MOVEMotor

buggy = MOVEMotor()

while True:
    leftSensor = buggy.readLineSensor("l")
    rightSensor = buggy.readLineSensor("r")
    difference = abs(leftSensor - rightSensor) # (1)!
    if difference > 20: # (2)!
        if leftSensor > rightSensor: # (3)!
            buggy.motorOn("l", "f", 30)
            buggy.motorOff("r")
        else:
            buggy.motorOn("r", "f", 30)
            buggy.motorOff("l")
    else:
        buggy.motorOn("l", "f", 30)
        buggy.motorOn("r", "f", 30)
```

1. We only care about the difference between the two sensor readings, so we can use `abs()` to get the absolute value of the difference which means we don't have to worry about negative numbers.
2. You can change the value `20` to change how tolerant your program is to differences in sensor reading.
3. Turn right because the left sensor is no longer on the black line.

The line sensor will give a low value if it senses a dark surface and a high value if the surface is light.