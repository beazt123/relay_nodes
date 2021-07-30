from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node11",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos1/dds",
                "pub_topic": "/pos1/rover"}
            ]
        ),
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node22",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos2/dds",
                "pub_topic": "/pos2/rover"}
            ]
        ),
         Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node33",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos3/dds",
                "pub_topic": "/pos3/rover"}
            ]
        ),
        Node(
            package="relay_nodes",
            node_executable="pub",
            node_name="relay_node44",
            output="screen",
            # emulate_tty=True,
            parameters=[
                {"sub_topic": "/pos4/dds",
                "pub_topic": "/pos4/rover"}
            ]
        ),
    ])
