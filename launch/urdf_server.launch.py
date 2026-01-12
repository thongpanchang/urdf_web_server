#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_dir = get_package_share_directory('ur_description')
    
    return LaunchDescription([
        Node(
            package='urdf_web_server',
            executable='cors_server',
            name='urdf_web_server',
            output='screen',
            parameters=[{
                'port': 8000,
                'bind': '0.0.0.0',
                'package_dir': pkg_dir
            }]
        )
    ])
