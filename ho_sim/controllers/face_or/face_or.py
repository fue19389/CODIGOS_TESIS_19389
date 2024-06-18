from controller import Robot
import tensorflow as tf
import numpy as np
import cv2
import threading
import faceLANDMARKS as fL


class wModel:
    def __init__(self):
      
        self.TIME_STEP = 32
        self.MAX_SPEED = 6.28
        lipdif = 0.0

        self.ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
        self.ho_model = tf.keras.models.load_model(self.ho_model)

        self.robot = Robot()

        self.leftMotor = self.robot.getDevice('left wheel motor')
        self.rightMotor = self.robot.getDevice('right wheel motor')
        self.leftMotor.setPosition(float('inf'))
        self.rightMotor.setPosition(float('inf'))
        self.detector = fL.FaceMeshDetector()



    def on(self):

        def run_on():
            self.CAP = cv2.VideoCapture(0)
            cont = 0
            oldcont = 0
            SPEEDC = 0
            flag = 0
            flagp = 0

            while True:
                _, imgF = self.CAP.read()
                img, nodes = self.detector.findFaceMesh(imgF)
                nodes = np.array([nodes])
                if nodes.any() != 0:
                    xlip = (nodes[0][13][0]) - (nodes[0][14][0])
                    ylip = (nodes[0][13][1]) - (nodes[0][14][1])
                    lipdif = ((xlip ** 2) + (ylip ** 2)) ** 0.5
                    y_predicted = self.ho_model.predict(nodes, verbose=None)
                    prediction = int(np.argmax(y_predicted))
                else:
                    prediction = 1
                    lipdif = 0.0




                if lipdif < 0.03:
                    if prediction == 0:
                        if SPEEDC != 0:
                            self.leftMotor.setVelocity(0.50 * SPEEDC * self.MAX_SPEED)
                            self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        else:
                            self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                            self.rightMotor.setVelocity(0.35 * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)

                    if prediction == 1:
                        self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        flag = 0
                        self.robot.stepBegin(self.TIME_STEP)

                    if prediction == 2:
                        if SPEEDC != 0:
                            self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                            self.rightMotor.setVelocity(0.50 * SPEEDC * self.MAX_SPEED)
                        else:
                            self.leftMotor.setVelocity(0.35 * self.MAX_SPEED)
                            self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)

                    if prediction == 3:
                        if flag == 0:
                            oldcont = cont
                            SPEEDC += 0.2
                            flag = 1
                        cont += 0.2
                        if abs(cont - oldcont) > 4.0:
                            SPEEDC += 0.05
                        if SPEEDC > 0.99:
                            SPEEDC = 0.99

                        self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)
                    else:
                        pass

                    if prediction == 4:
                        if flag == 0:
                            oldcont = cont
                            SPEEDC -= 0.2
                            flag = 1
                        cont -= 0.2
                        if abs(cont - oldcont) > 4.0:
                            SPEEDC -= 0.05
                        if SPEEDC < -0.99:
                            SPEEDC = -0.99

                        self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)
                    else:
                        pass

                    print(prediction, cont, SPEEDC, SPEEDC*self.MAX_SPEED)
                    self.robot.stepEnd()

                elif lipdif >= 0.03:
                    if SPEEDC > 0:
                        SPEEDC -= 0.2
                        if SPEEDC <= 0:
                            SPEEDC = 0
                        self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)
                    if SPEEDC < 0:
                        SPEEDC += 0.2
                        if SPEEDC >= 0:
                            SPEEDC = 0
                        self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                        self.robot.stepBegin(self.TIME_STEP)
                    else:
                        pass
                    print(prediction, cont, SPEEDC)
                    cont = 0
                    flag = 0


        on_thread = threading.Thread(target=run_on)
        on_thread.daemon = True
        on_thread.start()
    def stop(self):
        self.CAP.release()
        cv2.destroyAllWindows()