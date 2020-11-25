"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
import math
import numpy as np
import turtle

L = 0.105
x = 0
y = 0
angle = 0
vl = -3
vr = -5

vt = (vl+vr)/2
wp = (vr-vl)/L

C = np.array([[x], [y], [angle]])

# create the Robot instance.
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
rightMotor = robot.getMotor('wheel2')
leftMotor = robot.getMotor('wheel1')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

rightMotor.setVelocity(vr)
leftMotor.setVelocity(vl)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(64) != -1:
    A=np.array([[math.cos(C[2]), 0],[math.sin(C[2]), 0],[0, 1]])
    B=np.array([[vt],[wp]])
    D=C+A.dot(B)
    C=D
    
    an=(C[2]/math.pi)*180
    
    turtle.goto(values[0], values[1])
    turtle.setheading(an)
    
    pass
    
rightMotor.setVelocity(0)
leftMotor.setVelocity(0)
# Enter here exit cleanup code.
