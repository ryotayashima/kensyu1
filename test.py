#!/usr/bin/python
# -*- coding: utf-8 -*-
from core_tool import *
def Run(ct,*args):
    x = list(ct.robot.FK())
    # ct.robot.Q(x)
    # print ct.robot.Q(x)
    # ct.robot.FK(x)
    # print ct.robot.FK(x)
    print x
    q0 = [0]*7
    q0[0] = -0.022254568871029695
    q0[1] = 0.027604284836455075
    q0[2] = 0.022568074910412333
    q0[3] = -2.200118621520332
    q0[4] = -0.00047771840080773566
    q0[5] = 0.656946868009727
    q0[6] = 0.0010118998269884236
    ct.robot.MoveToQ(q0, 3.0, blocking = True)
