docker build -t ros2 -f dockerfile .

docker run -it \
    --privileged \
    --network=host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="${HOME}/ros2_ws:/root" \
    --name="ros2_container" \
    ros2:latest
    