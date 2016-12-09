import sys
import asyncio
import time

import cozmo
from cozmo.util import degrees, Pose

'''This is a script for Cozmo to draw characters.
'''

class Drawing:
    def __init__(self, *a, **kw):
        self.robot = None
        self.dictDraw = {'a':self.drawA, 'b':self.drawB,
                         'c':self.drawC, 'd':self.drawD,
                         'e':self.drawE, 'f':self.drawF,
                         'g':self.drawG, 'h':self.drawH,
                         'i':self.drawI, 'j':self.drawJ,
                         'k':self.drawK, 'l':self.drawL,
                         'm':self.drawM, 'n':self.drawN,
                         'o':self.drawO, 'p':self.drawP,
                         'q':self.drawQ, 'r':self.drawR,
                         's':self.drawS, 't':self.drawT,
                         'u':self.drawU, 'v':self.drawV,
                         'w':self.drawW, 'x':self.drawX,
                         'y':self.drawY, 'z':self.drawZ}
        cozmo.connect(self.run)

    def run(self, sdk_conn):
        '''The run method runs once Cozmo is connected.'''
        self.robot = sdk_conn.wait_for_robot()
        initPos = self.robot.pose;
        print(initPos)
        updatePos = initPos.position

        while True:
            # self.start_game(updatePos)
            char = input("Input a character").lower()
            print(char)
            self.dictDraw[char](updatePos, 0)

    def start_game(self, updatePos):
        find_face = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)
        try:
            face = self.robot.world.wait_for_observed_face(timeout=30)
            print("Found face", face)
        except asyncio.TimeoutError:
            print("Didn't find a face")
        finally:
            find_face.stop()

        if face is not None:
            anim = self.robot.play_anim("anim_sparking_success_01").wait_for_completed()
            self.robot.say_text("Hi, I am Cozmo. What is your name.").wait_for_completed()
            name = input("Input your name.").lower()
            print(name)
            self.robot.say_text("Oh, I know it.").wait_for_completed()
            self.robot.say_text("hahahahahahahahaha").wait_for_completed()

            # for i in range(len(name)):
            #     char = name[i]
            #     self.dictDraw[char](updatePos, 0)
            char = name[0]
            self.dictDraw[char](updatePos, 0)
            
            self.robot.say_text("Do you like it, " + name).wait_for_completed()
            self.robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceWinSession).wait_for_completed()
            time.sleep(3)
            self.robot.say_text("Nice to meet you, " + name).wait_for_completed()
            self.robot.say_text("Bye,bye." + name).wait_for_completed()
        

    def drawA(self, updatePos, offset):
        print("A")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(-25)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1.2)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.4)
        self.robot.turn_in_place(degrees(50)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.2)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.turn_in_place(degrees(-130)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.7)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawB(self, updatePos, offset):
        print("B")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(20)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.7)
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-115)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawC(self, updatePos, offset):
        print("C")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-160)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawD(self, updatePos, offset):
        print("D")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.turn_in_place(degrees(160)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(60)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawE(self, updatePos, offset):
        print("E")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.1)
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset-40, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.5)
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        #self.robot.say_text("This is, E").wait_for_completed()
        self.robot.go_to_pose(initPos, relative_to_robot=False).wait_for_completed()

    def drawF(self, updatePos, offset):
        print("F")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.0)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawG(self, updatePos, offset):
        print("G")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-160)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(160)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawH(self, updatePos, offset):
        print("H")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.7)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.7)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.7)
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1.1)
        self.robot.set_lift_height(0.5).wait_for_completed()    

    def drawI(self, updatePos, offset):
        print("I")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        #self.robot.say_text("This is, I").wait_for_completed()

    def drawJ(self, updatePos, offset):
        print("J")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.4)
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.75)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawK(self, updatePos, offset):
        print("K")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1.1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.go_to_pose(Pose(updatePos.x+10, updatePos.y+offset+70, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(-30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(200, 200, duration=0.4)
        self.robot.turn_in_place(degrees(60)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        #self.robot.say_text("This is, K").wait_for_completed()

    def drawL(self, updatePos, offset):
        print("L")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.0)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.4)
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.7)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawM(self, updatePos, offset):
        print("M")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.7)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(40)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        #self.robot.say_text("This is, M").wait_for_completed()
    
    def drawN(self, updatePos, offset):
        print("N")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-30)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawO(self, updatePos, offset):
        print("O")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.9)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(25)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawP(self, updatePos, offset):
        print("P")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(45)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawQ(self, updatePos, offset):
        print("Q")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.9)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.7)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawR(self, updatePos, offset):
        print("R")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.turn_in_place(degrees(170)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(45)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-170)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawS(self, updatePos, offset):
        print("S")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(130)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(130)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(110)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.85)
        self.robot.turn_in_place(degrees(-50)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(130)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(110)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawT(self, updatePos, offset):
        print("T")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()
        #self.robot.say_text("This is, T").wait_for_completed()

    def drawU(self, updatePos, offset):
        print("U")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.turn_in_place(degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.turn_in_place(degrees(100)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.85)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawV(self, updatePos, offset):
        print("V")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawW(self, updatePos, offset):
        print("W")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.4)
        self.robot.turn_in_place(degrees(70)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.4)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.9)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawX(self, updatePos, offset):
        print("X")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=1)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawY(self, updatePos, offset):
        print("Y")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(30)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.turn_in_place(degrees(-70)).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.45)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.6)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.6)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.5)
        self.robot.turn_in_place(degrees(40)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.55)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()

    def drawZ(self, updatePos, offset):
        print("Z")
        self.robot.set_lift_height(0.5).wait_for_completed()
        # self.robot.go_to_pose(Pose(updatePos.x, updatePos.y+offset, updatePos.z, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()
        self.robot.turn_in_place(degrees(90)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.8)
        self.robot.turn_in_place(degrees(-135)).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=0.3)
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(400, 400, duration=1.2)
        self.robot.set_lift_height(0.5).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.3)
        self.robot.turn_in_place(degrees(135)).wait_for_completed()
        self.robot.set_lift_height(0.1).wait_for_completed()
        self.robot.drive_wheels(-400, -400, duration=0.8)
        self.robot.set_lift_height(0.5).wait_for_completed()


if __name__ == '__main__':
    cozmo.setup_basic_logging()
    Drawing()
