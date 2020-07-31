#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import String
from tf.transformations import euler_from_quaternion
def callback(data):
    for x in range(len(data.name)):
        if  x==13 or x==14 or x==15 or x==16:
            orien=data.pose[x].orientation
            orien_list=[orien.x, orien.y,orien.z,orien.w]
            (roll,pitch,yaw)=euler_from_quaternion(orien_list)
            #prediction to the next second
            new_p={'x':data.pose[x].position.x+data.twist[x].linear.x*1,
                  'y':data.pose[x].position.y+data.twist[x].linear.y*1,
                  'theta':yaw+data.twist[x].angular.z*1}
            dynamic_obs={data.name[x]:new_p}
            print(dynamic_obs)
            #print(new_p)
            #dynamic_obs[data.name[x]]=new_p
            #print(data.pose[x].position.x)
            #print(data.name[x])
            #print(data.twist[x])
    #print(data.name)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gazebo/model_states", ModelStates, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
