1)git clone this repo
2)build the docker file using the following command:
    docker build -t imageName .
3)create a container of the image using the following commands:
    docker run -it --name containerName imageName
4) at this you can run the following command in the terminal you are currently in: 
    ros2 run py_pubsub talker
5)you should see the publisher running at this point in the terminal
6) open up a new terminal to set up the subscriber
7) once you are in the new terminal, run the following commands:
   docker exec -it containerName /bin/bash -c "source /opt/ros/humble/setup.bash && source /ros2_ws/install/setup.bash && ros2 run py_pubsub listener"
