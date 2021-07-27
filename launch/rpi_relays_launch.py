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
                {"sub_topic": "/pos1/rpi",
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
                {"sub_topic": "/pos2/rpi",
                "pub_topic": "/pos2/dds"}
            ]
        ),
         Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node3",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos3/rpi",
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
                {"sub_topic": "/pos4/rpi",
                "pub_topic": "/pos4/dds"}
            ]
        ),
    ])