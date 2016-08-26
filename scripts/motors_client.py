#!/usr/bin/env python

import sys
import rospy
from motors.srv import *

def two_motors_client(x, y):
    rospy.wait_for_service('motors')
    try:
        motors = rospy.ServiceProxy('motors', pins)
        resp1 = motors(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting pin %s with state %s"%(x, y)
    two_motors_client(x, y)
    print "done !"
