#!/bin/bash
set -e

# Source ROS 2 and workspace environments
source /opt/ros/humble/setup.bash
source /ros2_ws/install/setup.bash

exec "$@"
