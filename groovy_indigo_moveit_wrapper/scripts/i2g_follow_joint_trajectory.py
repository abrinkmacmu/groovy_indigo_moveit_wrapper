#! /usr/bin/env python
import sys
import roslib
roslib.load_manifest('groovy_control_msgs')
roslib.load_manifest('control_msgs')
import actionlib
import rospy

import control_msgs.msg as cm
import groovy_control_msgs.msg as gcm
import groovy_trajectory_msgs.msg as gtm 


class Server:
  def __init__(self, action, client):
    self.server = actionlib.SimpleActionServer(action, cm.FollowJointTrajectoryAction, self.execute, False)
    self.server.start()
    self.client = client

  def execute(self, goal):
    client_goal = gcm.FollowJointTrajectoryGoal()
    #print client_goal.trajectory.header
    #print "received goal"
    #print goal.trajectory.header
    client_goal.trajectory.header = goal.trajectory.header
    client_goal.trajectory.joint_names = goal.trajectory.joint_names
    for point in goal.trajectory.points:
	    newPoint = gtm.JointTrajectoryPoint()
	    newPoint.positions     = point.positions
	    newPoint.velocities    = point.velocities
	    newPoint.accelerations = point.accelerations
	    newPoint.time_from_start = point.time_from_start
	    client_goal.trajectory.points.append(newPoint)
    client_goal.path_tolerance = goal.path_tolerance
    client_goal.goal_tolerance = goal.goal_tolerance
    client_goal.goal_time_tolerance = goal.goal_time_tolerance

    client.send_goal(client_goal)
    if client.wait_for_result():
    	res = client.get_result()
    	print res
    	self.server.set_succeeded()
    else:
    	print "Result was unsuccessful"
    	self.server.set_aborted()
    

if __name__ == '__main__':
	rospy.init_node('i2g_follow_joint_trajectory_node')

	indigo_action = rospy.get_param("~indigo_action", "default_indigo_action")
	groovy_action = rospy.get_param("~groovy_action", "default_groovy_action")

	client = actionlib.SimpleActionClient(groovy_action, gcm.FollowJointTrajectoryAction)
	server = Server(indigo_action, client)