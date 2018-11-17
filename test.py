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
    x0 = []
    x0 = [0.65000972128356476, 0.0, 0.50002246981734688, 0.0, 0.70709699833427231, 0.0, 0.70711656385243649]
    ct.robot.MoveToX(x0, 3.0, blocking = True)
