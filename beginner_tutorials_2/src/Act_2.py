#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import re

class Act_2():
    def __init__(self):
        rospy.init_node('turtle_move', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def distance(self,goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.distance(goal_pose)

    def steering_angle(self,goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self,goal_pose, cst=2):
        return cst * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        data="  " 
        with open("../config/config3.yaml") as openfile:              
          for line in openfile:
            for part in line:
              if "x" in part:
               data=data+line
          #data=data[:data.index(',')] + data[data.index(',')+1:]
              elif "y" in part:
               data=data+line
        temp = re.findall(r'\d+',data) 
        res = list(map(int, temp))
        print("Script en cours d'execution")
        goal_pose = Pose()
        for i in range(0,6,2):
          goal_pose.x = float(res[i]) 
          goal_pose.y = float(res[i+1])
          print(goal_pose.x)
          print(goal_pose.y)
          distance_tolerance = 0.01
          vel_msg = Twist()

        while self.distance(goal_pose) >= distance_tolerance:
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()
        print("Press Ctrl+Z to interrupt")

if __name__ == '__main__':
    try:
        x = Act_2()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass
