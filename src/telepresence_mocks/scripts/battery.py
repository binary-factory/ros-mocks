#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
import random

pub = rospy.Publisher('battery_lvl', UInt8, queue_size=10)
rospy.init_node('battery12V')
r = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():
   pub.publish(random.randint(0,255))
   r.sleep()
