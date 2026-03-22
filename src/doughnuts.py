import rclpy    # ROS2 Python client library
import rclpy.node import Node   # ROS2 Node class
from geometry_msgs.msg import Twist  # Import the twist message  

class DoughnutNode(Node): # This class is the node
    def __init__(self):
        super().__init__('doughnut_node')  # init to initialise the node with a name
        #ros2 topic pub /cmd_vel geometry_msgs/Twist "linear:
    
        self.publisher_ = self.create_publisher(
            Twist, # Message type
            '/cmd_vel', # Topic name
            10 # Queue size buffer
        )

        self.timer = self.create_timer(0.1, self.publish_cmd) # Create a timer to call the publish_cmd function every 0.1 seconds
  
    def publish_cmd(self):
        msg = Twist() # Create the message

        #convert the yaml
        #Linear:
        linear.x = 0.5 #Linear: x: 0.5 y: 0.0 z: 0.0
        linear.y = 0.0
        linear.z = 0.0

        #angular
        angular.x = 0.0 #Angular: x: 0.0 y: 0.0 z: 0.5
        angular.y = 0.0
        angular.z = 5.0

    def main(args=None):
        rclpy.init(args=args) # Start ROS2
        node = DoughnutNode() # Create the node 
        rclpy.spin(node) # Keep the node alive and running 

        node.destroy_node() 
        node.shutdown() # Shutdown ROS2

    if __name__ == '__main__':
        main()