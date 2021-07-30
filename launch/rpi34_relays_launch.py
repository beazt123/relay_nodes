from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node3",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos3",
                "pub_topic": "/pos3/dds"}
            ]
        ),
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node4",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos4",
                "pub_topic": "/pos4/dds"}
            ]
        ),
    ])
