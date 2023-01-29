import rclpy
from rclpy.node   import Node
import math
from tf2_ros import *
import tf_transformations
import geometry_msgs.msg
from tf2_ros import TransformBroadcaster  
from tribot_interface.config import tf_pid
import numpy as np
from simple_pid import PID


class Tribot_rmtt_tf_node(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
        self.target_frame = rclpy.get_param('~target_frame')
        self.follower_robot_name = rclpy.get_param('~follower_robot_name')
        self.set_distance = rclpy.get_param('~set_distance')

        self.listener = self.TransformListener()

        self.follower_vel = rclpy.Publisher(self.follower_robot_name + '/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)

        self.rate = rclpy.Rate(10.0)

        self.pid_linear_x = PID(1, 0.0, 0.0)
        self.pid_linear_x.output_limits = (-0.5, 0.5)
        self.pid_linear_y = PID(1, 0.0, 0.0)
        self.pid_linear_y.output_limits = (-0.5, 0.5)
        self.pid_angular = PID(2, 0.0, 0.0)
        self.pid_angular.output_limits = (-1.5, 1.5)

        while rclpy.ok():                            # ROS2系统是否正常运行
            try:
                (trans, rot) = self.listener.lookupTransform(self.follower_robot_name+'/base_link', self.target_frame, rclpy.Time())
            except (tf2.LookupException, tf2.ConnectivityException, tf2.ExtrapolationException):
                continue

            angular=self.pid_angular(tf_transformations.euler_from_quaternion(rot)[2])
            linear_x=self.pid_linear_x(trans[0])
            linear_y=self.pid_linear_y(trans[1])

            if abs(linear_x) < 0.02:
                linear_x = 0

            if abs(linear_y) < 0.02:
                linear_y = 0


            msg = geometry_msgs.msg.Twist()
            msg.linear.x = linear_x
            msg.linear.y = linear_y
            msg.angular.z = angular
            self.follower_vel.publish(msg)

            self.rate.sleep()

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = Tribot_rmtt_tf_node("tribot_rmtt_tf")   # 创建ROS2节点对象并进行初始化
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口

