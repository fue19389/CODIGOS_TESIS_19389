import serial
import threading
import tensorflow as tf
import numpy as np
import cv2
import faceLANDMARKS as fL


class Use_BT_MODEL:
    def __init__(self):

        self.ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
        self.ho_model = tf.keras.models.load_model(self.ho_model)
        self.detector = fL.FaceMeshDetector()
        self.BT = None
        self.CAP = None

    def on(self):
        def run_on():
            prediction = 1
            try:
                self.BT = serial.Serial('COM4', 115200)
                print('Conexión exitosa')
            except:
                print('Error de conexión')

            self.CAP = cv2.VideoCapture(0)
            while True:
                predictionold = prediction
                _, imgF = self.CAP.read()
                img, nodes = self.detector.findFaceMesh(imgF)
                nodes = np.array([nodes])
                if nodes.any() != 0:
                    xlip = (nodes[0][13][0]) - (nodes[0][14][0])
                    ylip = (nodes[0][13][1]) - (nodes[0][14][1])
                    lipdif = ((xlip ** 2) + (ylip ** 2)) ** 0.5
                    lipdif = round(lipdif, 3)
                    y_predicted = self.ho_model.predict(nodes, verbose=None)
                    prediction = int(np.argmax(y_predicted))
                else:
                    prediction = 1
                    lipdif = 0.0

                if prediction != predictionold:
                    realp = predictionold
                else:
                    realp = prediction

                data_string = str(realp) + ',' + str(lipdif) + '/'
                self.BT.write(data_string.encode())

                print(data_string)


        on_thread = threading.Thread(target=run_on)
        on_thread.daemon = True
        on_thread.start()

    def stop(self):

        prediction = 1
        lipdif = 0.0
        data_string = str(prediction) + ',' + str(lipdif) + '/'
        self.BT.write(data_string.encode())
        self.BT.close()
        self.CAP.release()
        cv2.destroyAllWindows()