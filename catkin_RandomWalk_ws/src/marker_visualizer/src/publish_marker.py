#! /usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker

rospy.init_node('rviz_marker')

marker_pub = rospy.Publisher("/marker_test", Marker, queue_size = 2)

marker = Marker()

marker.header.frame_id = "map"
marker.header.stamp = rospy.Time.now()

marker.type = 2
marker.id = 0

marker.scale.x = 0.5
marker.scale.y = 0.5
marker.scale.z = 0.5

marker.color.r = 0.0
marker.color.g = 0.0
marker.color.b = 1.0
marker.color.a = 1.0

marker.pose.position.x = 5
marker.pose.position.y = 2
marker.pose.position.z = 0

marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 1.0

while not rospy.is_shutdown():
  marker_pub.publish(marker)
  rospy.rostime.wallsleep(1.0)
