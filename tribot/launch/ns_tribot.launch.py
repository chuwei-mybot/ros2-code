import os
 
from ament_index_python.packages import get_package_share_directory
 
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
 
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
 
from launch.actions import DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
 
def generate_launch_description():
   robot_name = LaunchConfiguration('robot_name')
   robot_name_launch_arg = DeclareLaunchArgument(
        'robot_name',
        default_value='tribot1'
        #description='configure the namespace'
    )

   param_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('tribot'), 'launch'),
         '/param_name.launch.py'])
      )
   tribot_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('tribot'), 'launch'),
         '/tribot.launch.py'])
      )
   gazebo_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('tribot'), 'launch'),
         '/view_tribot_world.launch.py'])
      )
   kinematic_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('tribot'), 'launch'),
         '/set_kinematic.launch.py'])
      )
   
   node_with_namespace = GroupAction(
     actions=[
         PushRosNamespace(robot_name),
         param_node,
         tribot_node,
         gazebo_node,
         kinematic_node,
         robot_name_launch_arg,
      ]
   )
   
   return LaunchDescription([
      
      node_with_namespace
      
   ])