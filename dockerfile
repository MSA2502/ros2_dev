FROM ros:humble

# install ros package
RUN apt-get update && apt-get install -y \
      ros-${ROS_DISTRO}-desktop && \
    rm -rf /var/lib/apt/lists/* 
# launch ros package
CMD ["bash"]
#CMD ["ros2", "launch", "demo_nodes_cpp", "talker_listener_launch.py"]
##