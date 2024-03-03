!!! note

    For each coded solution below you may need to tweak the arguments such as the speed and the sleep time to fit your robot. Programming your robot to turn by an exact number of degrees is very difficult so just aim to move it in roughly the correct direction.

## **Lesson 1**

### Making the robot move back and forth

Program your robot to move forward for 3 seconds then stop and reverse back to where it started.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/414f2321311b4345892350d83c23c988){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    buggy.motorOn("l", "f", 25)
    buggy.motorOn("r", "f", 25)
    sleep(3000)
    buggy.motorOn("l", "r", 25)
    buggy.motorOn("r", "r", 25)
    sleep(3000)
    buggy.stopMotors()
    ```

---

## **Lesson 2**

### Task 1

Program your robot to move forward for 2 seconds, turn roughly 90° clockwise then continue moving forward.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/13e71a16d8be45a58a79e592d1d5bbba){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    buggy.motorOn('r', 'f', 25)
    ```

### Task 2

Program your robot to move forward for 2 seconds, turn roughly 180° clockwise then continue moving forward.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/163ff47bbaa8418eb48943ad754c8f86){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.motorOn('r', 'r', 25)
    sleep(900)
    buggy.motorOn('r', 'f', 25)
    ```

### Task 3

Program your robot to move up and down a line forever.  
  
*It is fine if it doesn't move in an exact line because it may not turn exactly 180° each time.*

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/4428cb1cdc08443c868aa9227f4649c6){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        buggy.motorOn('l', 'f', 25)
        buggy.motorOn('r', 'f', 25)
        sleep(2000)
        buggy.motorOn('r', 'r', 25)
        sleep(900)
    ```

### Task 4

Program your robot to move in the path of a square once then stop.

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.stopMotors()
    ```

### Task 5

Program your robot to move in the path of a square forever.  
  
*Use a while True: loop*

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/be625819bb2e4c62947822063a5db3d3){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        buggy.motorOn('l', 'f', 25)
        buggy.motorOn('r', 'f', 25)
        sleep(2000)
        buggy.motorOn('r', 'r', 25)
        sleep(450)
    ```

### Task 6

Program your robot to move like a snake.  
  
*Refer to the image on OneNote for what the path should look like*

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    #go forward
    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    #turn left 90 deg
    buggy.motorOn('l', 'r', 25)
    sleep(450)
    #go forward
    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    #turn left 90 deg
    buggy.motorOn('l', 'r', 25)
    sleep(450)
    #go forward
    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    #turn right 90 deg
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    #go forward
    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    #turn right 90 deg
    buggy.motorOn('r', 'r', 25)
    sleep(450)
    #go forward
    buggy.motorOn('l', 'f', 25)
    buggy.motorOn('r', 'f', 25)
    sleep(2000)
    buggy.stopMotors()
    ```

### Task 7

Program your robot to move in a zigzag path forever.

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        buggy.motorOn('l', 'f', 25)
        buggy.motorOn('r', 'f', 25)
        sleep(2000)
        #turn left 90 deg
        buggy.motorOn('l', 'r', 25)
        sleep(450)
        buggy.motorOn('l', 'f', 25)
        buggy.motorOn('r', 'f', 25)
        sleep(2000)
        #turn right 90 deg
        buggy.motorOn('r', 'r', 25)
        sleep(450)
    ```

---

## **Lesson 3 - Ultrasonic Sensor**

### Task 1

Program your robot to move forward until it detects an object within a 10cm range in front of it, at which point it stops moving.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/c300bacd554f49ea863810fbcbc52897){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True: 
        distance = buggy.measureDistance() 
        if distance > 10:
            buggy.motorOn("l", "f", 25)
            buggy.motorOn("r", "f", 25)
        else:
            buggy.stopMotors()
    ```

### Task 2

Program your robot to beep its horn when it detects an object within a 20cm range in front of it.

??? tip "Hint"

    Using your program from task 1, add an if statement in your `while True` loop that calls `buggy.beepHorn()` if the distance is less than 20.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/9528bc62bcd24d8791763b3c0746aa95){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True: 
        distance = buggy.measureDistance()
        if distance < 20:
            buggy.beepHorn()
        if distance > 10:
            buggy.motorOn("l", "f", 25)
            buggy.motorOn("r", "f", 25)
        else:
            buggy.stopMotors()
    ```

### Task 3

Program your robot to slow down its speed when it detects an object within a 10-20cm range in front of it. Your program should stop moving when there is an object within a 10cm range in front.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/37ab89b6021d4da78a011fbecb010605){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True: 
        distance = buggy.measureDistance()
        if distance > 20:
            buggy.motorOn("l", "f", 25)
            buggy.motorOn("r", "f", 25)
        elif distance <= 20 and distance > 10:
            buggy.motorOn("l", "f", 20)
            buggy.motorOn("r", "f", 20)
        else:
            buggy.stopMotors()
    ```

### Task 4

Program your robot to change direction, by turning 90° to the right, when it detects an object within a 10cm range in front of it.

??? tip "Hint"

    Using the code from task 1, replace the code after the `else` statement with code that will turn the robot 90° to the right.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](https://parsons.problemsolving.io/puzzle/426c24a385de40d8ae233f205b034fd8){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True: 
        distance = buggy.measureDistance()
        if distance > 10:
            buggy.motorOn("l", "f", 25)
            buggy.motorOn("r", "f", 25)
        else:
            buggy.motorOn('r', 'r', 25)
            sleep(450)
    ```

### Extension Task 1

Make your robot alternate between turning left and turning right when it detects an object within a 10cm range in front of it.

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    left = True # (1)!

    while True: 
        distance = buggy.measureDistance()
        if distance > 10:
            buggy.motorOn("l", "f", 25)
            buggy.motorOn("r", "f", 25)
        else:
            if left:
                buggy.motorOn("l", "r", 25)
                buggy.motorOn("r", "f", 25)
            else:
                buggy.motorOn("l", "f", 25)
                buggy.motorOn('r', 'r', 25)
            sleep(450)
            left = not left # (2)!
    ```

    1. `left` is a boolean value that represents whether the robot is due to turn left.
    2. After turning the boolean value for `left` is flipped so that if it turned right, it will turn left next time.

## **Lesson 4 - Line Sensor**

???+ note

    Make sure you have followed the tutorial for programming your robot to follow a black line first. The tutorial can be found [at this link](https://bo-wen-zhang.github.io/Kitronik-MOVE-Motor/tutorials/#using-the-line-following-sensor).

### Task 1

Program your robot to be able to follow a black line but stop moving when an object is within a 10cm range in front of it.

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        leftSensor = buggy.readLineSensor("l")
        rightSensor = buggy.readLineSensor("r")
        difference = abs(leftSensor - rightSensor)
        distance = buggy.measureDistance()
        if distance <= 10:
            buggy.stopMotors()
        elif difference > 20: 
            if leftSensor > rightSensor: 
                buggy.motorOn("l", "f", 30)
                buggy.motorOff("r")
            else:
                buggy.motorOn("r", "f", 30)
                buggy.motorOff("l")
        else:
            buggy.motorOn("l", "f", 30)
            buggy.motorOn("r", "f", 30)
    ```

### Task 2

Program your robot to randomly stop moving for 2 seconds while it is following a line. Once the robot continues moving again it should carry on following a line.

???+ tip "Hint"

    During each iteration of the `while True:` loop you can generate a random number using `randint()` from the `random` module and make the program wait for 2 seconds if the random number is equal to a specified number.

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor
    from random import randint

    buggy = MOVEMotor()

    while True:
        randomNumber = randint(1, 1000) #(1)!
        if randomNumber == 1000: # (2)!
            buggy.stopMotors()
            sleep(2000)
        
        leftSensor = buggy.readLineSensor("l")
        rightSensor = buggy.readLineSensor("r")
        difference = abs(leftSensor - rightSensor)

        if difference > 20: 
            if leftSensor > rightSensor: 
                buggy.motorOn("l", "f", 30)
                buggy.motorOff("r")
            else:
                buggy.motorOn("r", "f", 30)
                buggy.motorOff("l")
        else:
            buggy.motorOn("l", "f", 30)
            buggy.motorOn("r", "f", 30)
    ```

    1. Generate a random number between 1 to 1000 (inclusive)
    2. If the random number is 1000 then we will stop moving for 2 seconds.

### Task 3

Program your robot to be able to follow a black line and speed up or slow down when the buttons on the micro:bit are pressed.

???+ tip "Hint"

    Your speed should be stored in a variable to make it easy to change its value whenever a button on the micro:bit is pressed.

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    speed = 30

    while True:
        if button_a.was_pressed():
            speed = speed + 1
        elif button_b.was_pressed():
            speed = speed - 1     
            
        leftSensor = buggy.readLineSensor("l")
        rightSensor = buggy.readLineSensor("r")
        difference = abs(leftSensor - rightSensor)

        if difference > 20: 
            if leftSensor > rightSensor: 
                buggy.motorOn("l", "f", speed)
                buggy.motorOff("r")
            else:
                buggy.motorOn("r", "f", speed)
                buggy.motorOff("l")
        else:
            buggy.motorOn("l", "f", speed)
            buggy.motorOn("r", "f", speed)
    ```

## **Lesson 5 - Input**

### Task 1

Program the robot so that when button A is pressed both of the motors are powered on, and when button B is pressed the motors are turned off.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](parsons_puzzles/lesson5task1.html){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        if button_a.was_pressed():
            buggy.motorOn("l", "f", 30)
            buggy.motorOn("r", "f", 30)
        elif button_b.was_pressed():
            buggy.stopMotors()
    ```

### Task 2

Program the robot so that when button A is pressed the robot spins clockwise, and when button B is pressed the robot spins counter-clockwise instead.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](parsons_puzzles/lesson5task2.html){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        if button_a.was_pressed():
            buggy.motorOn("l", "f", 30)
            buggy.motorOn("r", "r", 30)
        elif button_b.was_pressed():
            buggy.motorOn("l", "r", 30)
            buggy.motorOn("r", "f", 30)
    ```

### Task 3 

Program the robot to move forward forever. If button A is pressed the robot should speed up by 10, if button B is pressed the robot should slow down by 10.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](parsons_puzzles/lesson5task3.html){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    speed = 20
    while True:
        if button_a.was_pressed():
            speed = speed + 10
        elif button_b.was_pressed():
            speed = speed - 10
        buggy.motorOn("l", "f", speed)
        buggy.motorOn("r", "f", speed)
    ```

### Task 4

Program the robot so that pressing button A will make the robot move forward for 1 second then stop and pressing button B will make the robot move backward for 1 second then stop.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](parsons_puzzles/lesson5task4.html){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()

    while True:
        if button_a.was_pressed():
            buggy.motorOn("l", "f", 30)
            buggy.motorOn("r", "f", 30)
            sleep(1000)
            buggy.stopMotors()
        elif button_b.was_pressed():
            buggy.motorOn("l", "r", 30)
            buggy.motorOn("r", "r", 30)
            sleep(1000)
            buggy.stopMotors()
    ```

### Task 5

Program the robot so that button A controls whether the right motor is on or off and button B controls whether the left motor is on or off.  
When a motor is on, it should be in the forward direction.  
If the right motor is on then pressing button A should turn it off, but if the motor is off and button A is pressed then the motor should turn on.

??? tip "Parson's Puzzle"

    [Open Parson's Puzzle in a new tab](parsons_puzzles/lesson5task5.html){ .md-button .md-button--primary target="_blank"}

??? success "Code solution"

    ```{.python .no-copy .code-font .no-select linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    leftMotorIsOn = False
    rightMotorIsOn = False

    while True:
        if button_a.was_pressed():
            if rightMotorIsOn:
                buggy.motorOff("r")
            else:
                buggy.motorOn("r", "f", 30)
            rightMotorIsOn = not rightMotorIsOn
        elif button_b.was_pressed():
            if leftMotorIsOn:
                buggy.motorOff("l")
            else:
                buggy.motorOn("l", "f", 30)
            leftMotorIsOn = not leftMotorIsOn
    ```

## **Lesson 6 - Display**

!!! note

    To display an image to the LED grid you need to use `display.show(NAME_OF_IMAGE)` and replace `NAME_OF_IMAGE`

### Task 1

Copy and paste the program found [here](https://bo-wen-zhang.github.io/Kitronik-MOVE-Motor/tutorials/#using-the-ultrasonic-sensor){target="_blank"} into your editor. Extend the program to make the micro:bit display an X on the LED grid when the robot stops moving. When the robot is moving the LED grid should display a check mark.

Use `display.show(Image.NO)` for the image of X.  
Use `display.show(Image.YES)` for the image of a check mark.

### Task 2

Modify your program from task 1 and make your robot light up your own image while it is moving forward.

???+ success "Example of creating a custom image of a square"

    ```{.python .code-font linenums="1" title="main.py"}
    from microbit import *
    square = Image("99999:"
                   "90009:"
                   "90009:"
                   "90009:"
                   "99999")

    display.show(square)
    ```

### Task 3

Copy and paste the program found [here](https://bo-wen-zhang.github.io/Kitronik-MOVE-Motor/tutorials/#moving-back-and-forth){target="_blank"} into your editor. Extend the program to make the chassis LEDs blue when the robot is moving forward and red when it is moving backward.

???+ success "Example of lighting the chassis LEDs green"

    ```{.python .code-font linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    buggy.setAllLED("green")
    buggy.showLEDs()
    ```

### Task 4

Copy and paste the program found [here](https://bo-wen-zhang.github.io/Kitronik-MOVE-Motor/tutorials/#using-the-line-following-sensor){target="_blank"} into your editor. Extend the program so that when button A is pressed all of the chassis LEDs turn purple and when button B is pressed they all turn orange.

???+ success "Reminder of how to use the buttons on the micro:bit"

    ```{.python .code-font linenums="1" title="main.py"}
    from microbit import *
    from KitronikMOVEMotor import MOVEMotor

    buggy = MOVEMotor()
    while True:
        if button_a.was_pressed():
            # code to execute when button A is pressed
    ```

### Task 5

Extend the program from task 4 to make the robot display on the LED grid the direction that it is moving. It should show an up arrow when it is moving forward, and a left/right arrow when it is turning left/right.

The images that you need are:  
`Image.ARROW_N`  
`Image.ARROW_E`  
`Image.ARROW_W`