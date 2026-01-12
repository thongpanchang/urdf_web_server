#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import rclpy
from rclpy. node import Node
import sys
import os

class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

class URDFServerNode(Node):
    def __init__(self):
        super().__init__('urdf_web_server')
        self.get_logger().info('🚀 Starting URDF Web Server')
        
        # Get parameters
        self.declare_parameter('port', 8000)
        self.declare_parameter('bind', '0.0.0.0')
        self.declare_parameter('package_dir', '')
        
        port = self.get_parameter('port').value
        bind = self. get_parameter('bind').value
        pkg_dir = self.get_parameter('package_dir').value
        
        if pkg_dir:
            os.chdir(pkg_dir)
            self.get_logger().info(f'📂 Serving from: {pkg_dir}')
        
        # Start HTTP server
        self.httpd = HTTPServer((bind, port), CORSHandler)
        self.get_logger().info(f'📡 Server:  http://{bind}:{port}')
        self.get_logger().info('🔐 CORS:  Enabled')
        
    def serve(self):
        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            self. get_logger().info('👋 Server stopped')
            self.httpd.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = URDFServerNode()
    node.serve()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
