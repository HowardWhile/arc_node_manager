# Readme

ros2 node manager



## Download



```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/HowardWhile/arc_node_manager.git
```



## Build

```shell
cd ~/ros_ws
# colcon build 
colcon build --packages-select arc_node_manager
```



##  Run

```bash
source ~/ros2_ws/install/setup.bash
ros2 run arc_node_manager node_manager
```



## Develop

- VS Code

```
cd ~/ros2_ws/src/arc_node_manager/
code .
```

- Qt Creator

```shell
cd ~/ros2_ws/src/arc_node_manager/
qtcreator arc_node_manager.pyproject
```



