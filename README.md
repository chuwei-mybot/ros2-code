#启动leader小车
$ros2 launch tribot leader_tribot.launch.py 
#启动跟随小车tribot1
$ros2 launch tribot tribot_spawn_robot1.launch.py robot_name:tribot1
#启动leader小车的键盘控制节点
$ros2 run tribot tribot_teleop
#启动tribot1的tf广播节点
$ros2 run tribot tf_broadcaster1
#启动tribot1的运动控制节点
$ros2 run follower_kinematic1   #之后关闭第8行代码中的tf广播节点
#启动跟随小车tribot2
$ros2 launch tribot tribot_spawn_robot2.launch.py robot_name:tribot2
#启动tribot2的tf广播节点
$ros2 run tribot tf_broadcaster2
#启动tribot2的运动控制节点
$ros2 run follower_kinematic2   #之后关闭第14行代码中的tf广播节点
