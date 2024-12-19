# ZED-mobile-cleaning-simulated-robot.
Fisrt step in building the differential-drive ZED mobile cleaning robot:

Create your ros2 workspace (You can use any name for your workspace, but follow naming rules.)
```
mkdir ros_ws 
```
```
cd ros_ws
```
Create your src folder

```
mkdir src
```

In the src directory of your workspace clone the repo in it to work with robot pkg.
```
cd src
```

```
  git clone https://github.com/Oyefusi-Samuel/ZED-mobile-cleaning-simulated-robot..git
```
If you build the workspace and you see some errors pop up .You should upgrade pytest to a version that is 6.2 or higher. Use the following command
```
  pip install --upgrade pytest
```
Then build the workspace again:
```
  colcon build
```
**Source the workspace**
```
source install/setup.bash
```

**STEPS TO TAKE TO GET THE ROBOT UP AND READY:**
1. Lauch the robot in an empty world  

2. Visualize in Rviz .

Launch the Node:   (To visualize the robot in an empty gazebo world)
```
 ros2 launch robot show.robot.launch.py use_sim_time:=true
```
![Screenshot from 2024-12-19 13-42-21](https://github.com/user-attachments/assets/04351a44-f6eb-4d3c-ab1c-bc062457ad40)

Launch the rviz Node:   (To visualize the robot joint, tf)
```
  ros2 launch robot display.launch.py 
```
![Screenshot from 2024-12-19 13-54-59](https://github.com/user-attachments/assets/992d408c-3ccf-4444-8ea9-5433f56b6bfe)

**The centre of the robot is the "base_link".**

Plugins used in simulation of the robot can be gotten from:
https://classic.gazebosim.org/tutorials?tut=ros_gzplugins

**spawning the robot into a custom gazebo world:**
     To spawn the robot into gazebo, launch the file called show.robot.launch.py (Note: launch files in ROS 2 are python scripts/files)
 Command:
 ```
   ros2 launch robot show.robot.launch.py
 ```
 Check if the topics are available.This list all topics which are available:
 ```
   ros2 topic list
 ```
 Now,we can drive the robot around once we use the teleop_twist_keyboard node to publish to the "/cmd_vel" topic that the robot subscribes to.
 
 ```
   ros2 run teleop_twist_keyboard  teleop_twist_keyboard
 ```
 
 You can give colour to the robot,by adding colour to the .xacro file.Video decription below,while using the teleop_twist_keyboard to drive the robot.
 

 ```
   cd src
 ```
 
 ```
   ros2 pkg create drive_robot --build-type ament_python --dependencies rclpy
 
 ```
 Run the node in the pasckage to make the robot drive forward, in linear of x.
 ```
   ros2 run drive_robot velocity_drive
 ```

# LAUNCHING SAVED GAZEBO WORLD WITH ROBOT SPAWNED IN IT.
 ```
    ros2 launch robot show.robot.launch.py world:='path to where you saved your Gazebo world'
 ```
 ![Screenshot from 2023-03-07 16-57-01](https://user-images.githubusercontent.com/97457075/223492102-4b27dd07-a5f6-4b56-91f1-b20b52a065ba.png)
![Screenshot from 2023-03-07 17-02-44](https://user-images.githubusercontent.com/97457075/223492458-2b3d6ffe-db92-44e4-8a41-42573fa984d6.png)

You can check the TF2 TREE:
```
  ros2 run rqt_tf_tree rqt_tf_tree
```
![Screenshot from 2023-03-08 19-52-28](https://user-images.githubusercontent.com/97457075/223807831-64f8f7f3-c000-4d08-82b0-b4725c639a14.png)

# To LAUNCH THE WORLD:
 
```
   ros2 launch robot show.robot.launch.py world:="path to the .world file"
```
Mine is:
```
  ros2 launch robot show.robot.launch.py world:=/home/magnum/simuate_ws/src/robot/worlds/new.world
```
Outdoor 3D vision world


```
  ros2 launch robot show.robot.launch.py world:=/home/robothrone/new_robogpt/ros2slam_ws/src/Ros-2-simulated-robot./worlds/outside_world.world 
```

![Screenshot from 2023-03-08 23-10-51](https://user-images.githubusercontent.com/97457075/223862718-2ca56db5-4b6a-4a9e-a5b2-625d82918a81.png)

# SLAM 
Run the slam_toolbox node.
```
  ros2 launch robot online_async.launch.py 
```
[Screencast from 03-09-2023 11:21:33 AM.webm](https://user-images.githubusercontent.com/97457075/224001965-dfaaf7e7-9660-437a-94b4-5b78740142ad.webm)

# AUTONOMOUS NAVIGATION:
 Localization:
 ```
    ros2 launch robot localization.launch.py map:=/home/magnum/simuate_ws/src/robot/maps/offline.yaml  use_sim_time:=true
```
But if you want to use the localization mode (AMCL) you have to specify the path in which your map.yaml file is located and pass it into map:=""

-  ros2 launch robot localization.launch.py map:=""   use_sim_time:=true

Navigation Mode(NAV2 stack)
```
   ros2 launch  robot nav.launch.py use_sim_time:=true map_subscribe_transient_local:true
```
   We can also write a python script that publish certain velocity to make the robot move and also perform some basic task.
 Create a ROS 2 package called drive_robot ,its dependecies on rclpy,the package should be created in the src directory of your workspace.
 ```

  
[Screencast from 03-11-2023 05:26:36 PM.webm](https://user-images.githubusercontent.com/97457075/224503398-5ea5fe0c-618a-463e-9fa6-b0f82840eb19.webm)

# Converting Gazebo classic to Gazebo sim(Lastest Gazebo simulator)
Install required dependecies
```
  sudo apt install ros-<ros2_distro>-ros-gz
  sudo apt install ros-humble-twist-mux
  sudo apt install ros-humble-twist-stamper
  sudo apt install ros-humble-ros2-control
  sudo apt install ros-humble-ros2-controllers
```
## for example:
If you are using ros 2 humble distro , just replace <ros2_distro> with humble . So it will be :
```
  sudo apt install ros-humble-ros-gz
```





