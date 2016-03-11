from gpiozero import Motor
import time
#from gpiozero.Pin import
#import RPi.GPIO as GPIO

mr = Motor(3, 2)
ml = Motor(15, 14)
ml.stop()
mr.stop()

try:

    def forward():
        ml.forward(0.3)
        mr.forward(0.3)

    def backward():
        ml.backward(0.3)
        mr.backward(0.3)
        
    def sstop():
        ml.stop()
        mr.stop()

while(True):
    while(raw_input()=='w'):
        print "forward"
        forward()
        time.sleep(1)

    while(raw_input()=='s'):
        print "backward"
        backward()
        time.sleep(1)
    print "stopped"
    sstop()


