#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:53:26 2018

@author: kuba
"""

import turtle
def figurki(numofang, linelen):
    for dupsko in range(numofang):
        turtle.forward(linelen)
        turtle.right(360/numofang)
        