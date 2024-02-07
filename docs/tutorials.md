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

