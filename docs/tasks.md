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

## **Lesson 3**

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

??? success "Code solution"

    ```{.python .no-copy .no-select linenums="1" title="main.py"}
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