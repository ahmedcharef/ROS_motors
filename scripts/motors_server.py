#!/usr/bin/env python

from motors.srv import *
import rospy
import pyfirmata

PORT = '/dev/ttyACM0'
board = pyfirmata.Arduino(PORT)

def handle_two_motors(req):

    print "pin selected is pin %s with state is %s"%(req.a, req.b)
    board.digital[req.a].write(req.b) 
    board.digital[9].write(0)
    pin11 = board.get_pin('d:11:p')
    pin11.write(0.3)
    
    board.digital[6].write(1)
    board.digital[7].write(0)
    pin10 = board.get_pin('d:10:p')
    pin10.write(0.3)

 
#    board.pass_time(2) delay with 2 seconds 

    return pinsResponse(req.a + req.b)

def two_motors_server():
    rospy.init_node('two_motors__server')
    s = rospy.Service('motors', pins, handle_two_motors)
    print "Ready to control motors."
    rospy.spin()

if __name__ == "__main__":
    two_motors_server()
