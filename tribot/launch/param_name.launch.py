from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tribot',
            executable='param_name',
            name='declare_namespace_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'robot_name': 'tribot1'}
            ]
        )
    ])