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
