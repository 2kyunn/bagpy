import bagpy
from bagpy import bagreader

c = bagreader("/home/isr/rosbag/tiltedVLP_xsens_odom_zed/negative_obstacle.bag")
c.laser_data()