import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node

import xacro
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Configuration to check for sim time
    use_sim_time = LaunchConfiguration('use_sim_time')
    gui = LaunchConfiguration('gui')  # To toggle joint_state_publisher GUI

    # Define package path and URDF file
    pkg_path = os.path.join(get_package_share_directory('robot'))  # Replace 'robot' with your package name
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')  # Path to the .xacro file
    
    # Process the URDF file
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = robot_description_config.toxml()

    # Path to RViz config file
    rviz_config_file = os.path.join(pkg_path, 'config', 'robot_display.rviz')  # Place your RViz config in the config folder

    # Node for robot_state_publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': use_sim_time}]
    )

    # Node for joint_state_publisher (non-GUI version)
    joint_state_publisher_node = Node(
        condition=UnlessCondition(gui),
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # Node for joint_state_publisher GUI version
    joint_state_publisher_gui_node = Node(
        condition=IfCondition(gui),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    # Launch description
    return LaunchDescription([
        # Declare launch arguments
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation time if true'
        ),
        DeclareLaunchArgument(
            'gui',
            default_value='true',
            description='Enable joint_state_publisher GUI'
        ),

        # Add nodes to the launch description
        node_robot_state_publisher,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
