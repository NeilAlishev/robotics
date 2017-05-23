#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from std_msgs.msg import String

def my_moveit_method():
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('my_moveit_node',
                  anonymous=True)

  robot = moveit_commander.RobotCommander()
  scene = moveit_commander.PlanningSceneInterface()
  group = moveit_commander.MoveGroupCommander("left_arm")

  group.set_planning_time(10)

  print "CURRENT POSE"
  print group.get_current_pose()

  display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory,
                                    queue_size=20)

  rospy.sleep(10)

  # move hand in front of the robot
  pose_target1 = geometry_msgs.msg.Pose()
  pose_target1.orientation.x = 0.0236905488148
  pose_target1.orientation.y = -0.0178672483016
  pose_target1.orientation.z = 0.997796220371
  pose_target1.orientation.w = 0.0593483104086

  pose_target1.position.x = 0.328034637259
  pose_target1.position.y = 0.0814299109243
  pose_target1.position.z = 0.255088071269

  group.set_pose_target(pose_target1)
  plan1 = group.go(wait=True)

  # wait for Rviz to display plan1
  rospy.sleep(5)

  # move hand up
  pose_target2 = geometry_msgs.msg.Pose()
  pose_target2.orientation.x = 0.702323664605
  pose_target2.orientation.y = 0.0279592579776
  pose_target2.orientation.z = 0.0989923016684
  pose_target2.orientation.w = 0.70438645234

  pose_target2.position.x = 0.100413189685
  pose_target2.position.y = 0.423777941782
  pose_target2.position.z = 0.463426360506

  group.set_pose_target(pose_target2)

  plan2 = group.go(wait=True)

  # wait for Rviz to display plan2
  rospy.sleep(5)

if __name__=='__main__':
  try:
    my_moveit_method()
  except rospy.ROSInterruptException:
    pass