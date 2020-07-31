#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import String
from tf.transformations import euler_from_quaternion
def callback(data):
    for x in range(len(data.name)):
        if x==14:
            orien=data.pose[x].orientation
            orien_list=[orien.x, orien.y,orien.z,orien.w]
            (roll,pitch,yaw)=euler_from_quaternion(orien_list)
            print(roll,pitch,yaw)
            print(data.name[x])

    #print(data.name)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gazebo/model_states", ModelStates, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
