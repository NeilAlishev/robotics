#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

import time

def init_publishers():
	all_publishers = []
	all_publishers.append(rospy.Publisher('/ar601/Head1Roll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/Head2Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LAnklePitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LAnkleRoll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LArmPitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LElbowYaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LHipPitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LHipRoll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LHipYaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LKneePitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LShoulder1Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LShoulder2Roll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LShoulder3Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LWrist1Roll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/LWrist2Yaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/Neck1Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/Neck2Yaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RAnklePitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RAnkleRoll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RArmPitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RElbowYaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RHipPitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RHipRoll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RHipYaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RKneePitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RShoulder1Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RShoulder2Roll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RShoulder3Pitch_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RWrist1Roll_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/RWrist2Yaw_position_controller/command', Float64, queue_size=10))
	all_publishers.append(rospy.Publisher('/ar601/TorsoYaw_position_controller/command', Float64, queue_size=10))

	return all_publishers

def reset_robot():
	all_publishers = init_publishers()

	for publisher in all_publishers:
		publisher.publish(0.0)
		time.sleep(0.5)

def main():
	rospy.init_node('my_publisher_node', anonymous=True)
	reset_robot()

	pub1 = rospy.Publisher('/ar601/LShoulder2Roll_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/ar601/RShoulder2Roll_position_controller/command', Float64, queue_size=10)

	rate = rospy.Rate(0.5)
	flag = True
	while not rospy.is_shutdown():
		message = None

		if flag:
			message = 0.0
			flag = False
		else:
			message = 40.0
			flag = True

		pub1.publish(message)
		pub2.publish(-message)
		rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass