#The RPi.GPIO controls the GPIO interface on the Raspberry Pi and the time module represents time as code

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#Testing the first motor
L_IN1 = 20
L_IN2 = 21
L_PWM1 = 0

#Testing the second motor
L_IN3 = 22
L_IN4 = 23
L_PWM2 = 1

#Testing the third motor
R_IN1 = 24
R_IN2 = 25
R_PWM1 = 12

#Testing the fourth motor
R_IN3 = 26
R_IN4 = 27
R_PWM2 = 13

GPIO.setmode(GPIO.BCM)  

#Setting the MOTOR Driver Pin OUTPUT mode
GPIO.setup(L_IN1,GPIO.OUT)
GPIO.setup(L_IN2,GPIO.OUT)
GPIO.setup(L_PWM1,GPIO.OUT)

GPIO.setup(L_IN3,GPIO.OUT)
GPIO.setup(L_IN4,GPIO.OUT)
GPIO.setup(L_PWM2,GPIO.OUT)

GPIO.setup(R_IN1,GPIO.OUT)
GPIO.setup(R_IN2,GPIO.OUT)
GPIO.setup(R_PWM1,GPIO.OUT)

GPIO.setup(R_IN3,GPIO.OUT)
GPIO.setup(R_IN4,GPIO.OUT)
GPIO.setup(R_PWM2,GPIO.OUT)


GPIO.output(L_IN1,GPIO.LOW)
GPIO.output(L_IN2,GPIO.LOW)
GPIO.output(L_IN3,GPIO.LOW)
GPIO.output(L_IN4,GPIO.LOW)

GPIO.output(R_IN1,GPIO.LOW)
GPIO.output(R_IN2,GPIO.LOW)
GPIO.output(R_IN3,GPIO.LOW)
GPIO.output(R_IN4,GPIO.LOW)


#Set the pwm frequencey to 1000hz
pwm_R1 = GPIO.PWM(R_PWM1,100)
pwm_R2 = GPIO.PWM(R_PWM2,100)
pwm_L1 = GPIO.PWM(L_PWM1,100)
pwm_L2 = GPIO.PWM(L_PWM2,100)

#Set the inital duty cycle to 0
pwm_R1.start(0)
pwm_L1.start(0)
pwm_R2.start(0)
pwm_L2.start(0)

while True:
    GPIO.output(L_IN1,GPIO.LOW)  #Upper Left forward
    GPIO.output(L_IN2,GPIO.HIGH)
    pwm_L1.ChangeDutyCycle(50)
    GPIO.output(L_IN3,GPIO.HIGH)  #Lower left forward
    GPIO.output(L_IN4,GPIO.LOW)
    pwm_L2.ChangeDutyCycle(50)
    GPIO.output(R_IN1,GPIO.HIGH)  #Upper Right forward
    GPIO.output(R_IN2,GPIO.LOW)
    pwm_R1.ChangeDutyCycle(50)
    GPIO.output(R_IN3,GPIO.LOW)  #Lower Right forward
    GPIO.output(R_IN4,GPIO.HIGH)
    pwm_R2.ChangeDutyCycle(50)
    
#Stop pwm
pwm_R1.stop()
pwm_L1.stop()
pwm_R2.stop()
pwm_L2.stop()
sleep(1)

GPIO.cleanup()  #release all GPIO
