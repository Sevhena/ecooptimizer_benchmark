# long-message-chain snippets for rclpy

# File: /root/ecooptimizer/rclpy/rclpy/test/test_rosout_subscription.py
# Line: 85

logger = self.node.get_logger().get_child('child').get_child('grandchild')

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/action/server.py
# Line: 345

goal_info.stamp = self._node.get_clock().now().to_msg()

# ==================================================
