## 通过ros2 launch tribot leader_tribot.launch.py启动领导者小车leader_tribot
## 通过ros2 launch tribot tribot_spawn_robot.launch.py启动跟随的小车tribot1
## 通过ros2 run tribot tribot_teleop 启动键盘控制节点
## 通过ros2 run tribot tf_broadcaster启动tf播报
## 通过ros2 run tribot follower_kinematic启动跟随者运动控制节点
## 结束tf_broadcaster命令，小车可以正常控制

## 可视化：通过ros2 run plotjuggler plotjuggler打开plotjuggler,并订阅$$/gazebo/ModelState话题来显示小车位置
相关操作见[CSDN](https://shoufei.blog.csdn.net/article/details/124534170?spm=1001.2014.3001.5506)

## 目前问题：
## 没有完全解决参数传递问题，即无法通过命令行给跟随者小车增加命名空间
## tf_broadcaster.py文件存在问题（只能勉强运行）

