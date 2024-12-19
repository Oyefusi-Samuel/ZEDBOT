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
   
3. check the TF2 TREE

Launch the Node:   (To visualize the robot in an empty gazebo world)
```
 ros2 launch robot show.robot.launch.py use_sim_time:=true
```
![Screenshot from 2024-12-19 13-42-21](https://github.com/user-attachments/assets/a2b43c19-0088-4ea7-a876-66cb8e40df39)

Launch the rviz Node:   (To visualize the robot joint, tf)
```
  ros2 launch robot display.launch.py 
```
![Screenshot from 2024-12-19 13-58-04](https://github.com/user-attachments/assets/76c54e3a-6fae-48f9-943f-bee063887dfe)

You can check the TF2 TREE:
```
  ros2 run rqt_tf_tree rqt_tf_tree
```
![Screenshot from 2024-12-19 14-40-35](https://github.com/user-attachments/assets/11522d88-2ae8-4230-a877-e5301900e78e)

**The centre of the robot is the "base_link".**

# Plugins used in simulation of the robot can be gotten from:
https://classic.gazebosim.org/tutorials?tut=ros_gzplugins

![image](https://github.com/user-attachments/assets/051a698d-09ee-4850-af7f-0cbf6805c6f0)

# Spawning the robot into a custom gazebo world:
To spawn the robot into gazebo, launch the file called show.robot.launch.py, ensure you save the custom designed gazebo world into the world directory in the src folder (Note: launch files in ROS 2 are python scripts/files)


# To LAUNCH THE WORLD:
 
```
   ros2 launch robot show.robot.launch.py world:="path to the .world file"
```
Mine is:
```
ros2 launch robot show.robot.launch.py world:='/home/sam/zed_robot/src/robot/worlds/cafeworld' 
```
![Screenshot from 2024-12-19 14-09-51](https://github.com/user-attachments/assets/c2dca134-85bb-4497-a191-8be6e65ca0ef)
![Screenshot from 2024-12-19 14-24-43](https://github.com/user-attachments/assets/08396e2a-4be4-48c1-9304-a7ec9c649b3d)

```
ros2 launch robot show.robot.launch.py world:='/home/sam/zed_robot/src/robot/worlds/outside.world' 
```
![Screenshot from 2024-12-19 14-36-34](https://github.com/user-attachments/assets/7292b490-bbdb-45b0-a8c8-3f22dfdf448f)

 Check if the topics are available.This list all **topics** which are available:
 ```
   ros2 topic list
 ```
 Now,we can drive the robot around once we use the teleop_twist_keyboard node to publish to the **"/cmd_vel" topic** that the robot subscribes to.
 
 ```
   ros2 run teleop_twist_keyboard  teleop_twist_keyboard
 ```
 
 You can give colour to the robot,by adding colour to the robot description .xacro file.

![image](https://github.com/user-attachments/assets/7a46493f-694c-4e51-80fe-e2468c98deed)

 




# SLAM 
Run the slam_toolbox node.
```
  ros2 launch robot online_async.launch.py 
```
https://github.com/user-attachments/assets/1376903f-0d0d-4788-9e4d-83ada1f5b82a

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





