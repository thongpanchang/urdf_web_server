# urdf_server
this repo provide URDF server get /robot_description to Vizzy webapp

### How to install


### How to run
- Install this repo on ROS2 compute
- Install ROS rosbridge_server

```bash
# Install repo on ROS2 Compite
git clone https://github.com/thongpanchang/urdf_server.git
cd ws/
colcon build

# Install ROS rosbridge_server
sudo apt install ros-<ROS_DISTRO>-rosbridge-server
```
  
```bash
# State ros2 bridge server
ros2 launch rosbridge_server rosbridge_websocket_launch.xml websocket_address:=0.0.0.0

# Run robot description server
ros2 launch ur_description web_server.launch.py
```

### If your robot_description using xacro file. Plese convert xacro to urdf
```bash
# xacro to urdf command with ROS2
ros2 run xacro xacro $YOUR_ROBOT_.xacro > $YOUR_ROBOT_URDF_NAME.urdf

```
```bash
# And Checking the URDF when your converted
check_urdf $YOUR_ROBOT_URDF_NAME.urdf

check_urdf urdf_with_griper.urdf
# Output
robot name is: motoman_gp12_with_gripper
---------- Successfully Parsed XML ---------------
root Link: world has 1 child(ren)
    child(1):  base_link
        child(1):  base
        child(2):  link_1_s
            child(1):  link_2_l
                child(1):  link_3_u
                    child(1):  link_4_r
                        child(1):  link_5_b
                            child(1):  link_6_t
                                child(1):  tool0
                                    child(1):  tcp_virtual
                                    child(2):  gripper_base_link


```
