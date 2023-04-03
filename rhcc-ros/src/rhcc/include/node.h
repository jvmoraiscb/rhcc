#ifndef NODE_H
#define NODE_H

#include "falcon.h"
#include "geometry_msgs/Vector3.h"
#include "ros/ros.h"
#include "std_msgs/Int32.h"

class Node {
 private:
  Falcon falcon;
  ros::Publisher pub_pos;
  ros::Publisher pub_right_b;
  ros::Publisher pub_up_b;
  ros::Publisher pub_center_b;
  ros::Publisher pub_left_b;
  ros::Subscriber sub_force;
  int rate;

 public:
  Node(Falcon falcon, int rate, ros::NodeHandle n);
  void Run();
  void subCallback(const geometry_msgs::Vector3::ConstPtr& msg);
};

#endif  // NODE_H
