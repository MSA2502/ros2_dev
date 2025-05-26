### heading

You should take the following steps:

1)Git clone this repo. You can do so with the following command:
```sh
git clone https://github.com/MSA2502/docker.git
   ```

2)Build the docker file and run the docker file by execution buildRosh script. You can do by running the following commands:
 ```sh
chmod +x buildRos.sh
./ buildRos.sh
   ```

3)At this you can run the following command in the terminal you are currently in: 
 ```sh
ros2 run py_pubsub talker
   ```

4)You should see the publisher running at this point in the terminal

5)Open up a new terminal to set up the subscriber

6)Once you are in the new terminal, run the following command:
 ```sh
docker exec -it containerName /bin/bash -c "source /opt/ros/humble/setup.bash && source /ros2_ws/install/setup.bash && ros2 run py_pubsub listener"
   ```
