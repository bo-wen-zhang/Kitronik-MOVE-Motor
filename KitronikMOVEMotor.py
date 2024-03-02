# microbit-module: KitronikMOVEMotor@1.1.0
# Copyright (c) Kitronik Ltd 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# The code below has been modified and extended to fit teaching purposes.
# Copyright (c) Bo Wen Zhang 2024.

"""This module allows the user to interact with the Kitronik MOVE Motor.
"""

from microbit import i2c, pin1, pin2, pin3, pin8, pin12, pin13, pin14, pin15, pin16, display, sleep
from neopixel import NeoPixel
import machine
from time import sleep_us
import music

# Some useful constants
CHIP_ADDR = 0x62 # CHIP_ADDR is the standard chip address for the PCA9632, datasheet refers to LED control but chip is used for PWM to motor driver
MODE_1_REG_ADDR = 0x00
MODE_2_REG_ADDR = 0x01
MOTOR_OUT_ADDR = 0x08 # MOTOR output register address
MODE_1_REG_VALUE = 0x00 # Setup to normal mode and not to respond to sub address
MODE_2_REG_VALUE = 0x04  #Setup to make changes on ACK, outputs set to open-drain
MOTOR_OUT_VALUE = 0xAA  #Outputs set to be controled PWM registers

# Register offsets for the motors
LEFT_MOTOR = 0x04
RIGHT_MOTOR = 0x02

# Dictionary for mapping well known colours for LEDs from name to rgb decimal code
colourMap = {
    "red": (255, 0, 0),
    
    "orange": (255,165,0),
    
    "yellow": (255,255,0),
    
    "green": (0,128,0),
    
    "blue": (0, 0, 255),
    
    "cyan": (0, 255, 255),
    
    "violet": (238,130,238),
    
    "purple": (128,0,128),
    
    "white": (255, 255, 255),
    
    "black": (0, 0, 0),
}

LEFT = "l"
RIGHT = "r"
FORWARD = "f"
REVERSE = "r"

# Servo Constants
SERVO_MIN_PULSE_uS = 500
SERVO_MAX_PULSE_uS = 2500
SERVO_DEGREE_RANGE = 180
SERVO_DEG_TO_uS = (SERVO_MAX_PULSE_uS - SERVO_MIN_PULSE_uS) / SERVO_DEGREE_RANGE
SERVO_PWM_PERIOD_MS = 20

LEDS_NUMBER = 4

class MOVEMotor:
    """Class containing methods for controlling the :MOVE Motor.
    """

    def __init__(self):
        """
        Initializes a new MOVEMotor object and sets up the PCA (Printed Circuit Assembly) chip.

        Raises:
            OSError: microPython will likely raise OS error 19 if the MOVE Motor is off as it cannot talk to the I2C (Inter-Integrated Circuit) chip.
        """
        
        self._moveMotorVersion = 0
        display.clear()
        display.off()
        pin3.write_digital(1)
        sleep(100)
        if pin12.read_digital() == 1:
            pin3.write_digital(0)
            sleep(100)
            if pin12.read_digital() == 0:
                self._moveMotorVersion = 20
        
        display.on()
        buffer = bytearray(2)

        if self._moveMotorVersion == 0:
            try:
                buffer[0] = MODE_1_REG_ADDR
                buffer[1] = MODE_1_REG_VALUE
                i2c.write(CHIP_ADDR,buffer,False)
                readBuffer = i2c.read(CHIP_ADDR,1,False)
                if readBuffer[0] == MODE_1_REG_VALUE:
                    self._moveMotorVersion = 10
            except OSError:
                self._moveMotorVersion = 31
                self._ws2811 = NeoPixel(pin12, 2)
        
        if self._moveMotorVersion != 31:
            try:
                buffer[0] = MODE_1_REG_ADDR
                buffer[1] = MODE_1_REG_VALUE
                i2c.write(CHIP_ADDR,buffer,False)
                buffer[0] = MODE_2_REG_ADDR
                buffer[1] = MODE_2_REG_VALUE
                i2c.write(CHIP_ADDR,buffer,False)
                buffer[0] = MOTOR_OUT_ADDR
                buffer[1] = MOTOR_OUT_VALUE
                i2c.write(CHIP_ADDR,buffer,False)
            except OSError:
                raise OSError("Check the Micro:bit is turned on!")
        
        # setup PWM (pulse-width modulation) on the servo pin
        pin15.set_analog_period(SERVO_PWM_PERIOD_MS)
        pin16.set_analog_period(SERVO_PWM_PERIOD_MS)

        self._leds = NeoPixel(pin8, LEDS_NUMBER)

    def motorOn(self, motor: str, direction: str, speed: int):
        """
        Sets the requested motor running in the chosen direction at the set speed.
        At speeds lower than 20 the motor gets given a 'shove' at full speed to help it start.

        Args:
            motor (str): "l" for left, "r" for right
            direction (str): "f" for forward, "r" for reverse
            speed (int): speed between 0-100
        """
        speed = int(speed*2.55)
        if speed > 255:
            speed = 255
        elif speed < 0:
            speed = 0
        
        if self._moveMotorVersion != 31:
            # V1 to V2 :MOVE Motor
            motorForward = bytearray([0, 0])
            motorBackward = bytearray([0, 0])
            if motor == LEFT:
                motorForward[0] = LEFT_MOTOR
                motorBackward[0] = LEFT_MOTOR + 1
            elif motor == RIGHT:
                motorForward[0] = RIGHT_MOTOR + 1
                motorBackward[0] = RIGHT_MOTOR
            if direction == FORWARD:
                motorForward[1] = speed
            elif direction == REVERSE:
                motorBackward[1] = speed
            i2c.write(CHIP_ADDR, motorForward, False)
            sleep(1)
            i2c.write(CHIP_ADDR, motorBackward, False)
        
        else:
            # V3 :MOVE Motor
            motorBuf = bytearray([0, 0, 0])
            motorShove = bytearray([0, 0, 0])
            wsIndex = 0
            if motor == LEFT:
                wsIndex = 1
                if direction == FORWARD:
                    motorBuf[0] = speed
                    motorShove[0] = 60
                elif direction == REVERSE:
                    motorBuf[1] = speed
                    motorShove[1] = 60
            elif motor == RIGHT:
                wsIndex = 0
                if direction == FORWARD:
                    motorBuf[1] = speed
                    motorShove[1] = 60
                elif direction == REVERSE:
                    motorBuf[0] = speed
                    motorShove[0] = 60
            if 0 < speed < 26:
                #Gives the motor a 'shove' to aid starting on lower pwm ratios
                self._ws2811[wsIndex] = (3*motorShove[0]//4, 3*motorShove[1]//4, 3*motorShove[2]//4)
                self._ws2811.show()
                sleep(5)
            elif 26 <= speed < 51:
                self._ws2811[wsIndex] = (motorShove[0], motorShove[1], motorShove[2])
                self._ws2811.show()
                sleep(5)
            self._ws2811[wsIndex] = (motorBuf[0], motorBuf[1], motorBuf[2])
            self._ws2811.show()

    def motorOff(self, motor: str):
        """
        Stops a given motor.

        Args:
            motor (str): "l" for left, "r" for right
        """ 
        
        if self._moveMotorVersion != 31:
            # V1 to V2 :MOVE Motor
            stopBuffer = bytearray([0, 0])
            if motor == LEFT:
                stopBuffer[0] = LEFT_MOTOR
                i2c.write(CHIP_ADDR, stopBuffer, False)
                stopBuffer[0] = LEFT_MOTOR + 1
                i2c.write(CHIP_ADDR, stopBuffer, False)
            elif motor == RIGHT:
                stopBuffer[0] = RIGHT_MOTOR
                i2c.write(CHIP_ADDR, stopBuffer, False)
                stopBuffer[0] = RIGHT_MOTOR + 1
                i2c.write(CHIP_ADDR, stopBuffer, False)
        
        else:
            # V3 :MOVE Motor
            if motor == LEFT:
                self._ws2811[1] = (0, 0, 255)
            elif motor == RIGHT:
                self._ws2811[0] = (0, 0, 255)
            self._ws2811.show()

    def stopMotors(self):
        """
        Stops both the left and right motors.
        """
        
        self.motorOff(LEFT)
        self.motorOff(RIGHT)
        
    # Servo Control
    def writeServoDegree(self, servo: int, degrees: int):
        """
        Control the position of the selected servo using a given degree.

        Args:
            servo (int): Integer for servo 1 or 2, as per the chassis.
            degrees (int): Target position of the servo.
        """
        period = SERVO_MIN_PULSE_uS + (SERVO_DEG_TO_uS * degrees)
        self.writeServoPeriod(servo, period)
        
    def writeServoPeriod(self, servo: int, period: float):
        """
        Simulates an analogue output using PWW on the selected servo with a given period.

        Args:
            servo (int): Integer for servo 1 or 2, as per the chassis.
            period (float): Period of the PWN signal.
        """
        
        if servo < 1:
            servo = 1
        elif servo > 2:
            servo = 2
        if period < SERVO_MIN_PULSE_uS:
            period = SERVO_MIN_PULSE_uS
        elif period > SERVO_MAX_PULSE_uS:
            period = SERVO_MAX_PULSE_uS
        duty = round(period * 1024 * 50 // 1000000) #1024-steps in analog, 50Hz frequency, // to convert to uS
        if servo == 1:
            pin15.write_analog(duty)
        elif  servo == 2:
            pin16.write_analog(duty)
    
    def setLED(self, led: int, colour: str):
        """
        Set an LED on the MOVE Motor chassis to an given colour name. Only a selected range of colours available by name.

        Args:
            led (int): Integer between 0-3 indicating the LED to set.
            colour (str): Name of colour. Choose from: Red, Orange, Yellow, Green, Blue, Cyan, Violet, Purple, White, Black. 
        """
        colour = colour.lower()
        if colour not in colourMap:
            return
        
        rgb = colourMap[colour]
        
        self.setLEDByRGB(led, rgb)
    
    def setAllLED(self, colour: str):
        """
        Set all LEDs on the MOVE Motor chassis to an given colour name. Only a selected range of colours available by name.

        Args:
            colour (str): Name of colour. Choose from: Red, Orange, Yellow, Green, Blue, Cyan, Violet, Purple, White, Black. 
        """
        
        for i in range(LEDS_NUMBER):
            self.setLED(i, colour)
        
    def setLEDByRGB(self, led: int, rgb: 'tuple[int, int, int]'):
        """
        Set an LED on the MOVE Motor chassis to an RGB colour.

        Args:
            led (int): Integer between 0-3 indicating the LED to set.
            rgb (tuple[int, int, int]): RGB tuple representing the colour.
        """
        
        if led < 0:
            led = 0
        elif led > LEDS_NUMBER - 1:
            led = LEDS_NUMBER - 1
        self._leds[led] = rgb
        
    def setAllLEDByRGB(self, rgb: 'tuple[int, int, int]'):
        """
        Set all LEDs on the MOVE Motor chassis to an RGB colour.

        Args:
            rgb (tuple[int, int, int]): RGB tuple representing the colour.
        """
        
        for i in range(LEDS_NUMBER):
            self.setLEDByRGB(i, rgb)
    
    
    def showLEDs(self):
        """
        Show the LEDs. Must be called for any update to be visible.
        """
        
        self._leds.show()

    def brakeLightsOff(self):
        """
        Turn off the brake lights.
        """
        frontLeftColour = self._leds[0]
        frontRightColour = self._leds[1]
        self._leds.clear()
        self.setLEDByRGB(0, frontLeftColour)
        self.setLEDByRGB(1, frontRightColour)
        self.showLEDs()

    def beepHorn(self, duration: int =500):
        """
        Plays a horn sound for the duration (in ms) specified.

        Args:
            duration (int, optional): Defaults to 500ms.
        """
        
        music.pitch(185, duration=duration, wait=False)

    def measureDistance(self) -> int:
        """
        Measures distance (in cm) using the ultrasonic sensor.

        Returns:
            distance (int): Returns an integer representing the distance (in cm rounded down) of the object in front of the ultrasonic sensor. Returns -2 or -1 if there is an issue with reading the pulse.
        """
        pin13.set_pull(pin13.NO_PULL)
        pin13.write_digital(0)
        sleep_us(2)
        pin13.write_digital(1)
        sleep_us(10)
        pin13.write_digital(0)
        
        #From the HC-SR04 datasheet the formula for calculating distance is "microSecs of pulse"/58 for cm
        pulse = machine.time_pulse_us(pin14, 1, 500 * 58)
        distance = pulse // 58
        return distance

    
    def readLineSensor(self, sensor: str):
        """
        Measures and returns the reflectiveness of the surface below the selected line following sensor.

        Args:
            sensor (str): "l" or "r" for the left or right line following sensor.

        Returns:
            reflectiveness (int): An integer between 0-1023 indicating the reflectiveness of the surface below the line sensor. A dark surface is less reflective.
        """
        
        reflectiveness = 0
        if sensor == LEFT:
            reflectiveness = pin2.read_analog()
        elif sensor == RIGHT:
            reflectiveness = pin1.read_analog()
            
        return reflectiveness