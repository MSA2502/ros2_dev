import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import String


class StrActionServer(Node):

    def __init__(self):
        super().__init__('str_action_server')
        self._action_server = ActionServer(
            self,
            String,
            'str',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = String.Feedback()
        feedback_msg.partial_sequence = ["a", "b"]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = String.Result()
        result.sequence = feedback_msg.partial_sequence
        return result


def main(args=None):
    rclpy.init(args=args)

    str_action_server = StrActionServer()

    rclpy.spin(str_action_server)


if __name__ == '__main__':
    main()