from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node1",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos1",
                "pub_topic": "/pos1/dds"}
            ]
        ),
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node2",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos2",
                "pub_topic": "/pos2/dds"}
            ]
        ),
    ])
