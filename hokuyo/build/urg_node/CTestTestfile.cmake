# CMake generated Testfile for 
# Source directory: /home/neil/hokuyo/src/urg_node
# Build directory: /home/neil/hokuyo/build/urg_node
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
ADD_TEST(_ctest_urg_node_roslint_package "/home/neil/hokuyo/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/indigo/share/catkin/cmake/test/run_tests.py" "/home/neil/hokuyo/build/test_results/urg_node/roslint-urg_node.xml" "--working-dir" "/home/neil/hokuyo/build/urg_node" "--return-code" "/opt/ros/indigo/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/neil/hokuyo/build/test_results/urg_node/roslint-urg_node.xml make roslint_urg_node")
ADD_TEST(_ctest_urg_node_roslaunch-check_launch_urg_lidar.launch "/home/neil/hokuyo/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/indigo/share/catkin/cmake/test/run_tests.py" "/home/neil/hokuyo/build/test_results/urg_node/roslaunch-check_launch_urg_lidar.launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/neil/hokuyo/build/test_results/urg_node" "/opt/ros/indigo/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/neil/hokuyo/build/test_results/urg_node/roslaunch-check_launch_urg_lidar.launch.xml' '/home/neil/hokuyo/src/urg_node/launch/urg_lidar.launch' ")
