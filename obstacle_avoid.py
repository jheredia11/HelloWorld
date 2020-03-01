#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO          
from time import sleep
GPIO.cleanup()
#right motor 1
in1 = 24
in2 = 23
en1 = 25
temp1=1
#right motor 2
in3 = 17
in4 = 27
en2 = 22
temp2=1

#left motor 1
in5 = 10
in6 = 9
en3 = 11
temp3=1
#left motor2
in7 = 12
in8 = 16
en4 = 26
temp4=1

GPIO.setmode(GPIO.BCM)

#control motor

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(en1,1000)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(en2,1000)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
p3=GPIO.PWM(en3,1000)

GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(en4,GPIO.OUT)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)
p4=GPIO.PWM(en4,1000)

p1.start(25)
p2.start(25)
p3.start(25)
p4.start(25)

def controller(x):
        #x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1 & temp2==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         GPIO.output(in5,GPIO.HIGH)
         GPIO.output(in6,GPIO.LOW)
         GPIO.output(in7,GPIO.HIGH)
         GPIO.output(in8,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         GPIO.output(in5,GPIO.LOW)
         GPIO.output(in6,GPIO.HIGH)
         GPIO.output(in7,GPIO.LOW)
         GPIO.output(in8,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        temp1=1
        temp2=1
        temp3=1
        temp4=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.HIGH)
        temp1=0
        temp2=0
        temp3=0
        temp4=0
        x='z'
    elif x=='a':
        print("left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(20)
        p4.ChangeDutyCycle(20)
        temp1=1
        temp2=1
        temp3=1
        temp4=1
        x='z'

    elif x=='d':
        print("right")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        p1.ChangeDutyCycle(20)
        p2.ChangeDutyCycle(20)
        p3.ChangeDutyCycle(75)
        p4.ChangeDutyCycle(75)
        temp1=1
        temp2=1
        temp3=1
        temp4=1
        x='z'

    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)
        p4.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        p3.ChangeDutyCycle(50)
        p4.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(75)
        p4.ChangeDutyCycle(75)
        x='z'

def subscriber():
        sub = rospy.Subscriber('object_distance', Float32, callback_function)
        rate = rospy.Rate(1)
        rospy.spin()

def callback_function(message):
	rospy.loginfo("I received distance %d"%message.data)
 	x = 's'
        if (message.data > 30):
                x = 'f'
        elif(message.data<=30):
                x = 's'
                sleep(0.05)
                x = 'd'
                sleep(0.1)
                x = 'f'
                sleep(0.05)
                x = 'a'
                sleep(0.1)
                x = 'f'
                sleep(0.2)
                x = 'a'
                sleep(0.1)
                x = 'f'
                sleep(0.05)
                x = 'd'
                sleep(0.1)
        controller(x)

if __name__ == '__main__':
        rospy.init_node("simple_subscriber")
	subscriber()

GPIO.cleanup()
