#!/usr/bin/python
# -*- coding: utf-8 -*-
from core_tool import *
def Run(ct,*args):
    # 初期位置移動
    q0 = [0]*7
    q0[0] = -0.022254568871029695
    q0[1] = 0.027604284836455075
    q0[2] = 0.022568074910412333
    q0[3] = -2.200118621520332
    q0[4] = -0.00047771840080773566
    q0[5] = 0.656946868009727
    q0[6] = 0.0010118998269884236
    ct.robot.MoveToQ(q0, 8.0, blocking = True)
    rospy.sleep(2)
    # 初期位置固定
    x = list(ct.robot.FK())
    x0 = copy.deepcopy(x)
    # 腕を伸ばす
    x1 = copy.deepcopy(x0)
    # x1[0] += 0.3
    x1[0] = 0.4
    x1[1] = 0.1
    x1[2] = 0.19
    ct.robot.MoveToX(x1, 3.0, blocking = True)
    rospy.sleep(2)
    x2 = copy.deepcopy(x1)
    x2[0] = 0.5
    x2[1] = 0.1
    x2[2] = 0.19
    ct.robot.MoveToX(x2, 3.0, blocking = True)
    rospy.sleep(2)
    # グリッパーで掴む
    ct.robot.OpenGripper()
    ct.robot.MoveGripper(0.05)
    # 初期位置に戻る
    ct.robot.MoveToX(x0, 3.0, blocking = True)
    rospy.sleep(2)
    # 離す
    ct.robot.OpenGripper()
