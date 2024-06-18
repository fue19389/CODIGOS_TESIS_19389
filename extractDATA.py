# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código para transformar las fotos y labels de excel en datos utilizables

# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

import os
import cv2
import numpy as np
import pandas as pd


class GetModelData:

    def __init__(self):

        # ------------------------------------------------
        # ----- Seleccionar de datos ---------------------
        # ------------------------------------------------

        # Si se escoge etiquetas, guardar para modelos 0 -> 8

        self.nmodel = 9

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------

        # Se selecciona el archivo .xlsx dentro del repositorio
        self.lbldir = r"C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx"
        # Directorio para guardar las variables a exportar
        self.expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'
        # Directorio con carpetas de fotografias
        self.imgdir = r'C:\Users\gerar\PycharmProjects'

        # De esta manera solo se tienen que solicitar estos directorios y se aclara que
        # las carpetas de fotografías se llaman TRAINFACE y TESTFACE
        # El nombre de las variables exportadas aún lo tengo de manera fija

    # ------------------------------------------------
    # ----- Rutina extracción pixeles-----------------
    # ------------------------------------------------

    # Ahora se trabajará con el modelo 8 únicamente, cuando este listo será el original nada mas

    def prepareD(self, tsttrn):
        tsttrn = int(tsttrn)

        # Selección de carpeta de fotografías: entrenamiento o validación
        # Hoja y columna de excel
        # Nombres de array para datos de etiquetas y píxeles
        if tsttrn == 0:
            sheet = 'traintags'
            foldname = 'TRAINLIST'

            if self.nmodel == 0:
                col = 'A'
                yname = 'y_train'
                xname = 'x_train'
            if self.nmodel == 1:
                col = 'B'
                yname = 'y_train1'
                xname = 'x_train1'
            if self.nmodel == 2:
                col = 'C'
                yname = 'y_train2'
                xname = 'x_train2'
            if self.nmodel == 3:
                col = 'D'
                yname = 'y_train3'
                xname = 'x_train3'
            if self.nmodel == 4:
                col = 'E'
                yname = 'y_train4'
                xname = 'x_train4'
            if self.nmodel == 5:
                col = 'F'
                yname = 'y_train5'
                xname = 'x_train5'
            if self.nmodel == 6:
                col = 'G'
                yname = 'y_train6'
                xname = 'x_train6'
            if self.nmodel == 7:
                col = 'H'
                yname = 'y_train7'
                xname = 'x_train7'
            if self.nmodel == 8:
                col = 'I'
                yname = 'y_train8'
                xname = 'x_train8'
            if self.nmodel == 9:
                col = 'J'
                yname = 'y_train9'
                xname = 'x_train9'

        if tsttrn == 1:
            sheet = 'testtags'
            foldname = 'TESTLIST'

            if self.nmodel == 0:
                col = 'A'
                yname = 'y_test'
                xname = 'x_test'
            if self.nmodel == 1:
                col = 'B'
                yname = 'y_test1'
                xname = 'x_test1'
            if self.nmodel == 2:
                col = 'C'
                yname = 'y_test2'
                xname = 'x_test2'
            if self.nmodel == 3:
                col = 'D'
                yname = 'y_test3'
                xname = 'x_test3'
            if self.nmodel == 4:
                col = 'E'
                yname = 'y_test4'
                xname = 'x_test4'
            if self.nmodel == 5:
                col = 'F'
                yname = 'y_test5'
                xname = 'x_test5'
            if self.nmodel == 6:
                col = 'G'
                yname = 'y_test6'
                xname = 'x_test6'
            if self.nmodel == 7:
                col = 'H'
                yname = 'y_test7'
                xname = 'x_test7'
            if self.nmodel == 8:
                col = 'I'
                yname = 'y_test8'
                xname = 'x_test8'
            if self.nmodel == 9:
                col = 'J'
                yname = 'y_test9'
                xname = 'x_test9'

        # Crear la dirección de archivo desde el cual se extraen las fotografías
        tdir = os.path.join(self.imgdir, foldname)
        # Crear la dirección de guardado (con nombre) del archivo de pixeles
        xdir = os.path.join(self.expordir, xname)

        # Ceear lista del directorio de fotos
        xlist = os.listdir(tdir)
        # Obtener tamaño (cantidad de fotos)
        lenolist = int(len(np.array(xlist)))
        # Crear un array de ceros del tamaño de la lista
        x_t = np.zeros((lenolist, 180, 320, 3))

        # Guardado de datos de píxeles
        i = 0
        for filename in xlist:
            im = cv2.imread(os.path.join(tdir, filename))
            imr = cv2.resize(im, (320, 180))
            imr = cv2.cvtColor(imr, cv2.COLOR_BGR2RGB)
            x_t[i] = imr
            i = i + 1

        x_t = x_t.astype(int)
        np.save(xdir, x_t)

    # ------------------------------------------------
    # ----- Rutina creación archivo etiquetas --------
    # ------------------------------------------------

        # Crear la dirección de guardado (con nombre) del archivo de etiquetas
        ydir = os.path.join(self.expordir, yname)
        # Extraer el archivo de etiquetas desde una columna de excel
        y_t = np.array(pd.read_excel(self.lbldir, sheet_name=sheet, usecols=col))
        # Convertir el archivo de etiquetas para reducir tamaño
        y_t = y_t.astype(int)
        # Guardar el archivo de etiquetas
        np.save(ydir, y_t)
