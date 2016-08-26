# ROS_motors
Control DC motors with ROS usin H-Bridge L293D

# Installation
1- Put ROS_motors in a catkin workspace: See the catkin tutorial for details (http://wiki.ros.org/catkin/Tutorials/create_a_workspace). Use git to clone this repository into your workspace's "src/" directory. Or download ROS_motors as an archive and extract it to "src/"

2- Use rosdep (i.e. "rosdep install") to install missing dependencies. For details see (http://wiki.ros.org/ROS/Tutorials/rosdep)

To build ROS_motors go to your catkin workspace and execute "catkin_make". If you get an error about the missing siftgpu library, execute "catkin_make" again.

# Installation from Scratch
Assuming you have installed ROS hydro on Ubuntu, issue the following commands in a terminal (or copy-paste the whole sequence at once)

* Prepare Workspace
source /opt/ros/hydro/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
source devel/setup.bash

* Get ROS Motors
cd ~/catkin_ws/src
wget -q https://github.com/ahmedcharef/ROS_motors.git
cd ~/catkin_ws/

* Install
rosdep update
catkin_make
    catkin_make

# Installation done! What's next?
> roscore

> roscd ROS_motors

> chmod +x scripts/motors_client.py

> chmod +x scripts/motors_server.py

> rosrun ROS_motors motors_server.py

//request Arduino pin 13 with HIGH argument
> rosrun ROS_motors motors_client.py 11 1


