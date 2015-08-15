#!/usr/bin/env python
# references used: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)

    #node is publishing "cmd_val" topic
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    #initilasing a node named "talker"
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
	twist = Twist()
	twist.linear.x = 1
	twist.angular.z = 0.01;
	
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()

# ROSInterruptException can be thrown when we shutdown the process
# by ctrl+C
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
