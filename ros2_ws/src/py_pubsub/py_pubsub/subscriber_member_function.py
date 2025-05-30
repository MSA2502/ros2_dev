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


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription2 = self.create_subscription(
            Point,
            'topic1',
            self.listener_callback1,
            10)
        self.publisher3_ = self.create_publisher(String, 'topic2', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.j = 0
        self.subscription1  # prevent unused variable warning


    def timer_callback(self):
        msg3 = String()
        msg3.data = 'test: %d' % self.j
        self.publisher3_.publish(msg3)
        self.get_logger().info('Publishing: "%s"' % msg3.data)
        self.j += 1

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
    def listener_callback1(self, msg2):
        self.get_logger().info('I heard: "%s"' % msg2.x)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    #minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
