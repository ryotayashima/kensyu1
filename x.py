#!/usr/bin/python
import sys
sys.path.append('/home/yashima/ros_ws/ay_tools/ay_trick/ay_trick/scripts')
from core_tool import *
def Help():
  return '''Display current end effector pose (x,y,z,quaternion).
  Usage: q'''
def Run(ct,*args):
    #回転角から位置を計算
  return list(ct.robot.FK())
