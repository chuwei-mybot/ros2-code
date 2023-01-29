#!/usr/bin/env python

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


pid_linear = PID(2, 0.0, 0.0)
pid_linear.output_limits = (-0.5, 0.5)
pid_angular = PID(5, 0.0, 0.0)
pid_angular.output_limits = (-1.0, 1.0)

class Tribot_tf_node(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
        self.target_frame = rclpy.get_param('~target_frame')
        self.follower_robot_name = rclpy.get_param('~follower_robot_name')
        self.set_distance = rclpy.get_param('~set_distance')

        self.listener = self.TransformListener()

        self.follower_vel = rclpy.Publisher(self.follower_robot_name + '/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)

        self.rate = rclpy.Rate(10.0)
        
    #pid_linear.sample_time = pid_angular.sample_time = 0.1
        self.srv = self.create_service(tf_pid, self.callback)
        while rclpy.ok():                            # ROS2系统是否正常运行
            try:
                (trans, rot) = self.listener.lookupTransform(self.follower_robot_name+'/base_link', self.target_frame, rclpy.Time())
            except (tf2.LookupException, tf2.ConnectivityException, tf2.ExtrapolationException):
                continue

            dis = math.sqrt(trans[0] ** 2 + trans[1] ** 2)
            angular = pid_angular(-math.atan2(trans[1],trans[0]))
            linear =  pid_linear(self.set_distance - dis)

            if abs(linear) < 0.02:
                linear = 0

            msg = geometry_msgs.msg.Twist()
            msg.linear.x = linear
            msg.angular.z = angular
            self.follower_vel.publish(msg)

            self.rate.sleep()    # 休眠控制循环时间

    def callback(config, level):
        rclpy.loginfo("""Reconfigure Request: {linear_kp}, {linear_ki}, {linear_kd}, {angular_kp}, {angular_ki}, {angular_kd}""".format(**config))
        pid_linear.tunings = [float(config.get(key)) for key in ['linear_kp', 'linear_ki', 'linear_kd']]
        pid_angular.tunings = [float(config.get(key)) for key in ['angular_kp','angular_ki','angular_kd']]
        return config

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = Tribot_tf_node("tribot_tf")   # 创建ROS2节点对象并进行初始化
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口

