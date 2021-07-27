import rclpy
import rclpy.node
# from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from geometry_msgs.msg import PointStamped, Point

class RelayNode(rclpy.node.Node):
    def __init__(self):
        super().__init__('relay_node')

        self.get_logger().debug("Node initialised")

        # DECLARE PARAMETERS
        my_parameter_descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                        description='Example Description lolz')

        self.declare_parameter("sub_topic",
                                "/pos0/rpi",
                                my_parameter_descriptor)

        self.declare_parameter("pub_topic",
                                "/pos0/dds",
                                my_parameter_descriptor)
        self.get_logger().debug("Parameters declared")

        # GET PARAMETERS
        sub_topic = self.get_parameter("sub_topic").get_parameter_value().string_value
        pub_topic = self.get_parameter("pub_topic").get_parameter_value().string_value

        self.get_logger().debug("Parameters fetched")

        self.publisher = self.create_publisher(Point, pub_topic, 10)
        self.create_subscription(
                Point,
                sub_topic,
                self.listener_callback,
                10)

    def listener_callback(self, ps: Point):
        self.get_logger().info(f"{ps.x}, {ps.y}, {ps.z}")
        self.publisher.publish(ps)
'''

node = rclpy.node.Node(node_name)
my_parameter_descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                      description='This parameter is mine!')
node.declare_parameter("my_parameter",
                            "default value for my_parameter",
                            my_parameter_descriptor)

# GET PARAMETER


my_param = node.get_parameter("my_parameter").get_parameter_value().string_value

# SET PARAMETER
my_new_param = rclpy.parameter.Parameter(
            "my_parameter",
            rclpy.Parameter.Type.STRING,
            "world"
        )
        
all_new_parameters = [my_new_param]
node.set_parameters(all_new_parameters)

'''


    

def main():
    rclpy.init()
    print("Start")
    relayNode = RelayNode()
    print("set up node")
    rclpy.spin(relayNode)

    relayNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()