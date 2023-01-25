#通过ros2 launch tribot ns_tribot.launch.py启动所有节点，并加上命名空间
#通过ros2 run tribot tribot_teleop启动键盘控制节点
#可以用ros2 param set命令修改机器人命名空间（由参数robot_name控制）的名称

#目前问题：
#ns_tribot.launch.py文件中无法使用参数robot_name,只能直接使用PushRosNamespace(‘@@@’)命令，(@@@可以是tribot1等)，即舍弃robot_name参数；
而无法通过PushRosNamespace(robot_name)命令实时修改命名空间。
