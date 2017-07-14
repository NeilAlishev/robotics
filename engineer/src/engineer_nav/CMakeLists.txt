cmake_minimum_required(VERSION 2.8.3)
project(engineer_nav)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  dynamic_reconfigure
  geometry_msgs
  move_base_msgs
  nav_msgs
  roscpp
  rospy
  tf
  visualization_msgs
)
find_package(orocos_kdl REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES engineer_nav
#  CATKIN_DEPENDS actionlib dynamic_reconfigure geometry_msgs move_base_msgs nav_msgs roscpp rospy tf visualization_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)