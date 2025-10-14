from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from umath import acos, sin


# hub
hub = PrimeHub()
timer = StopWatch()
resetImu = lambda: hub.imu.reset_heading(0)
hub.system.set_stop_button(Button.BLUETOOTH)

# sensori
ultrasonic = UltrasonicSensor(Port.F)                                                   # porta sensore distanza 'F'
light = ColorSensor(Port.B)                                                             # porta sensore luce 'B'

# motori
motorMoveL = Motor(Port.D)                                                              # motore muovimento sinistro
motorMoveR = Motor(Port.E, Direction.COUNTERCLOCKWISE)                                  # motore muovimento destro
motorTopL = Motor(Port.C)                                                               # motore medio sinistro
motorTopR = Motor(Port.A)                                                               # motore medio destro
motorPair = DriveBase(motorMoveR, motorMoveL, wheel_diameter = 6, axle_track = 8.1)     # movimento con entrambi i motori

# costanti
IMU_ERROR = 1.15
MIN_POWER = 25
INCREMENT = 0.05

# variabili globali
brakeMove = True


############ FUNZIONI DI CONTROLLO ############

def enableImuCalib():
    """Enable IMU calibration"""
    hub.imu.settings(3,500)

def disableImuCalib():
    """Disable IMU calibration"""
    hub.imu.settings(0,0)

def calibImu(N,reset=True):
    """Imu calibration

        Calibrate the IMU N times. Each calibration takes 1 second.
        Each new calibration has less effect for calibrating the gyro.

        Parameters
        ----------
        N (int): Number of IMU calibration
        reset (bool): if true, reset the IMU
    """
    enableImuCalib()
    wait(N*1000+200) # 200ms more to be sure calibration is complete
    disableImuCalib()
    if reset:
        resetImu()

def motoriMain(power, targetAngle, kp):
    motorMoveR.dc(correction("L", power, targetAngle, kp))
    motorMoveL.dc(correction("R", power, targetAngle, kp))

def softStart(power, startPower):
    """softStart with coroutine.

        The function returns a dynamic value that increases
        over time.

        Parameters
        ----------
        power (int): Maximum power
        startPower (int): Start power
    """
    softStartPower = startPower
    
    yield startPower
    
    if (startPower < power):
        while (softStartPower < power):
            softStartPower += INCREMENT
            yield softStartPower
    if (startPower > power):
        while (softStartPower > power):
            softStartPower -= INCREMENT
            yield softStartPower

def softEnd(power):
    """softEnd with coroutine.

        The function returns a dynamic value that decreases
        over time.

        Parameters
        ----------
        power (int): Starting power
    """

    softEndPower = power
    while softEndPower > MIN_POWER:
        softEndPower -= INCREMENT
        yield softEndPower

def correction(motor, power, targetAngle, kp):
    """Proportional correction function for the direction.

        Used within the motor motion function,
        returns a power that corrects the direction of the robot.

        Parameters
        ----------
        motor (string): motor ("L" | "R")
        power (int): Power of the motor (-100, 100)
        targetAngle (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
    """

    gradiNow = hub.imu.heading()
    error = targetAngle - gradiNow

    p = kp * error

    correctedPower = 0

    if motor == "L":
        correctedPower = (abs(power) + p) if power > 0 else -(abs(power) - p)
    elif motor == "R":
        correctedPower = (abs(power) -p) if power > 0 else -(abs(power) + p)

    return correctedPower

def stopMotorPair():
    """Function to stop both motors"""
    motorMoveR.brake()
    motorMoveL.brake()

def checkExit():
    """Function to check if the button to exit program has been pressed"""
    if Button.BLUETOOTH in hub.buttons.pressed():
        wait(100)
        return True

############ FUNZIONI DI MOVIMENTO ############

def moveTime(time, power, targetAngle, kp, brake = True):
    """Function to move the motor with a proportional correction based on time

        Parameters
        ----------
        time -> ms (int): runtime of the function (ms)
        power -> % (int): Power of the motor (-100, 100)
        targetAngle -> ° (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
        brake (bool): if true, brakes after movement

    """

    global brakeMove

    power = softStart(power, 0 if brakeMove else (motorMoveL.speed() + motorMoveR.speed())/20)

    final_power = 0

    timer.reset()
    while timer.time() <= time:
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass
        
        motoriMain(final_power, targetAngle, kp)

    if brake:
        brakeMove = True
        stopMotorPair()
    else:
        brakeMove = False

def moveToLight(reflection, power, targetAngle, kp, brake = True, case=True):
    """Function to move the motor with a proportional correction based on the
    light

        Parameters
        ----------
        reflection -> % (int): Reflection detected by the light sensor (0, 100)
        power -> % (int): Power of the motor (-100, 100, %)
        targetAngle -> ° (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
        brake (bool): if true, brakes after movement
        case: boolean, optional (TRUE - lighter to darker, FALSE - darker to lighter)

    """
    global brakeMove
    
    power = softStart(power, 0 if brakeMove else (motorMoveL.speed() + motorMoveR.speed())/20)

    final_power = 0
    while light.reflection() <= reflection and case == False:
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass

        motoriMain(final_power, targetAngle, kp)

    while light.reflection() >= reflection and case == True:
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass

        motoriMain(final_power, targetAngle, kp)
    
    if brake:
        brakeMove = True
        stopMotorPair()
    else:
        brakeMove = False

def moveToDistance(distance, power, targetAngle, kp, brake = True):
    """Function to move the motor with a proportional correction based on the
    distance detected by the motor's encoder

        Parameters
        ----------
        distance -> cm (int): Distance detected by the motor's encoder
        power -> % (int): Power of the motor (-100, 100)
        targetAngle -> ° (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
        brake (bool): if true, brakes after movement

    """

    global brakeMove
    
    motorPair.reset()

    power = softStart(power, 0 if brakeMove else (motorMoveL.speed() + motorMoveR.speed())/20)

    final_power = 0 
    while abs(motorPair.distance()) <= abs(distance):
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass

        motoriMain(final_power, targetAngle, kp)

    if(brake==True):
        brakeMove = True
        stopMotorPair()
    else:
        brakeMove = False

def moveToDistanceUltrasound(distance, power, targetAngle, kp, brake = True):
    """Function to move the motor with a proportional correction based on the
    distance detected by the ultrasonic sensor

        Parameters
        ----------
        distance -> mm (int): Distance detected by the ultrasonic sensor
        power -> % (int): Power of the motor (-100, 100)
        targetAngle -> ° (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
        brake (bool): if true, brakes after movement

    """
    verso = 0
    if power > 0: verso = 1
    else: verso = -1

    global brakeMove

    power = softStart(power, 0 if brakeMove else (motorMoveL.speed() + motorMoveR.speed())/20)
    
    final_power = 0

    while (ultrasonic.distance() <= distance and verso == 1) or (ultrasonic.distance() >= distance and verso == -1):
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass

        motoriMain(final_power, targetAngle, kp)

    if brake:
        brakeMove = True
        stopMotorPair()
    else:
        brakeMove = False

def turnToAngle(powerL, powerR, targetAngle, kp):
    """Function to rotate the robot on an axis

            Parameters
            ----------
            powerL -> (int): Power of the left motor (-100, 100)
            powerR -> % (int): Power of the right motor (-100, 100)
            targetAngle -> ° (int): Angle of the robot to achieve (-360, 0, 360)
            kp (int): constant of correction (based on the power but 1 is the most used)
    """
    currentAngle = hub.imu.heading()
    diff = abs(currentAngle - targetAngle)
    gyroThreshold = 0

    rotationFlag = currentAngle <= targetAngle

    # softPowerL = softEnd(powerL)
    # softPowerR = softEnd(powerR)

    while (currentAngle <= targetAngle) if rotationFlag else (currentAngle >= targetAngle):
        if checkExit(): break
        
        currentAngle = hub.imu.heading()
        error = abs(currentAngle - targetAngle)

        # try:
        #     powerL = next(softPowerL)
        #     powerR = next(softPowerR)
        # except StopIteration:
        #     pass

        motorMoveR.dc(powerL * max(kp, error / diff))
        motorMoveL.dc(powerR * max(kp, error / diff))

        if error < gyroThreshold:
            break

    stopMotorPair()

def followLineTime(leftValue, rightValue, time, power, kp): # nero (sx) bianco (dx)
    """Function to follow a line for a certain amount of time

            Parameters
            ----------
            leftValue -> % (int) Reflection detected by the light
            sensor to keep on the left side of the sensor used (0, 100)
            rightValue -> % (int) Reflection detected by the light
            sensor to keep on the right side sensor used (0, 100)
            time -> ms (int): Runtime of the function (ms)
            power -> % (int): Power of the motor (-100, 100)
            kp (int): constant of correction (based on the power but 2 is the most used)
    """

    medium = (leftValue+rightValue)/2.0 # valore a metà

    timer.reset()
    while timer.time() <= time:
        reflection = light.reflection()
        direction = leftValue < rightValue
        kReflection = (kp*(medium-reflection ))

        motorMoveR.dc(power + kReflection if direction else power - kReflection)
        motorMoveL.dc(power - kReflection if direction else power + kReflection)

    stopMotorPair()

############ FUNZIONI CUSTOM ############

def cremagliera (distance, power, targetAngle, kp, height, kpSpeed, motorTop = 'L', resetAngle = True, brake = True):
    """Function to move the motor with a proportional correction based on the
    distance detected by the motor's encoder and sin motorTop movement

        Parameters
        ----------
        distance -> cm (int): Distance detected by the motor's encoder
        power -> % (int): Power of the motor (-100, 100)
        targetAngle -> ° (int): Angle of the robot (0, 360)
        kp (int): constant of correction (based on the power but 2 is the most used)
        height (int): target degree of max height of rack
        kpSpeed (int): costant of move speed correction (based on the power, around power*0.003)
        topMotor (char): which top motor we are going to use (by default it is 'L')
        brake (bool): if true, brakes after movement

    """

    global brakeMove

    motorPair.reset()
    
    if resetAngle:
        if motorTop == 'L': motorTopL.reset_angle()
        else: motorTopR.reset_angle()
    
    power = softStart(power, 0 if startFromStop else (motorMoveL.speed() + motorMoveR.speed())/20)

    final_power = 0 
    while abs(motorPair.distance()) <= abs(distance):
        if checkExit(): break

        try:
            final_power = next(power)
        except StopIteration:
            pass
        
        final_height = height * sin(acos(1-abs(motorPair.distance()/distance)))

        if motorTop == 'L': 
            motoriMain(final_power + kpSpeed * (motorTopL.angle() - final_height), targetAngle, kp)
        else: 
            motoriMain(final_power + kpSpeed * (motorTopR.angle() - final_height), targetAngle, kp)

        if (motorTop == 'L'):
            motorTopL.track_target(final_height)
        else:
            motorTopR.track_target(final_height)

    if(brake==True):
        stopMotorPair()
        startFromStop = True
    else:
        startFromStop = False



############ FUNZIONI DI DEBUG ############

def debug(txt):
    righe = txt.split('\n')
 
    for riga in righe:
        if riga == "":
            continue
        while not (Button.CENTER in hub.buttons.pressed()):
            wait(100)
        while Button.CENTER in hub.buttons.pressed():
            wait(100)
        eval(riga)

def waitPress():
    while not (Button.CENTER in hub.buttons.pressed()):
        wait(100)
    while Button.CENTER in hub.buttons.pressed():
        wait(100)