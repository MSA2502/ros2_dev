# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Point



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher1_ = self.create_publisher(String, 'topic', 10)
        self.publisher2_ = self.create_publisher(Point, 'topic1', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.subscription3 = self.create_subscription(
            String,
            'topic2',
            self.listener_callback2,
            10)
    def timer_callback(self):
        msg = String()
        msg2 = Point()
        msg.data = 'Hello World: %d' % self.i
        msg2.x = 5.5 + self.i
        self.publisher1_.publish(msg)
        self.publisher2_.publish(msg2)        
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.get_logger().info('Publishing: "%s"' % msg2.x)
        self.i += 1

    def listener_callback2(self, msg3):
        self.get_logger().info('I heard: "%s"' % msg3.data)

    
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    #min_pub = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    #rclpy.spin(min_pub)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    #min_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
