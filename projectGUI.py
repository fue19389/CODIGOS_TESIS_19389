# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código prueba para la GUI que involucra todos los otros códigos

# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

# Librerías para funciones
import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sn
import tensorflow as tf
from matplotlib import pyplot as plt
from matplotlib import rcParams

import feedDATA as fD
import extractDATA as eD
import photoMODEL as pM
import graphMODEL as gM
import liveTEST as lT
import sendBT as bT
import subprocess
webots_path = r'C:\Program Files\Webots\msys64\mingw64\bin\webotsw.exe'
webots_world = r'C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\ho_sim\worlds\ho_sim.wbt'
open_com = [webots_path, "--mode=fast", webots_world]
subprocess.Popen(open_com)

from ho_sim.controllers.face_or import face_or as fO

# Librerías para GUI
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


# ------------------------------------------------
# ----- Interfaz ---------------------------------
# ------------------------------------------------

class pGUI:


    def __init__(self):

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración Inicial ----------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        # Se crea la interfaz general
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        self.root = ctk.CTk()
        self.root.geometry('1000x625')
        self.root.title('HO GUI')

        # Se crea la selección de pestañas
        self.tabview = ctk.CTkTabview(self.root, width=900, height=575)
        self.tabview.add("Captura de fotografías")
        self.tabview.add("Manejo de datos")
        self.tabview.add('Prueba Turtle')
        self.tabview.add('Prueba Webots')
        self.tabview.add('Prueba ESP32/POLOLU')
        self.tabview.pack()

        # Inicialización de librerías personales
        self.feed = fD.ModelFeeder()
        self.ppr = eD.GetModelData()
        self.train = pM.ModelPhoto()
        self.train1 = gM.ModelGraph()
        self.use_m = lT.UseModel()
        self.use_bt = bT.Use_BT_MODEL()
        self.use_w = fO.wModel()

        # WEBOTS

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Captura de fotografías -----------------------------------
        # --------------------------------------------------------------------------------------------------------------


        self.btn1 = ctk.CTkButton(self.tabview.tab('Captura de fotografías'), text='CAPTURAR', font=('aptos', 30),
                                  width=350, height=150, command=self.actL)
        self.btn1.pack(padx=50, pady=50)

        self.label1 = ctk.CTkLabel(self.tabview.tab('Captura de fotografías'),
                                   text='Mueva la cabeza según las instrucciones audiovisuales \n (Punto de referencia en la luz de la cámara)',
                                   font=('aptos', 20))
        self.label1.pack(padx=20, pady=45)

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Manejo de datos ------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.label2 = ctk.CTkLabel(self.tabview.tab('Manejo de datos'), text='Escoja tipo de datos:', font=('aptos', 22))
        self.label2.pack(padx=15, pady=(20,0))

        self.buttonFrame2 = ctk.CTkFrame(self.tabview.tab('Manejo de datos'))

        self.btn_erase = ctk.CTkButton(self.buttonFrame2, text='Borrar Serie', font=('aptos', 18), width=250, height=75, command=self.erase)
        self.btn_erase.grid(row=0, column=0, padx=10, pady=10)

        self.btn_reset = ctk.CTkButton(self.buttonFrame2, text='Resetear Modelo', font=('aptos', 18), width=250, height=75, command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=10, pady=10)

        self.buttonFrame2.pack(pady=20)

        self.btn_train = ctk.CTkButton(self.tabview.tab('Manejo de datos'), text='Entrenar', font=('aptos', 18), width=250, height=75, command=self.trainM)
        self.btn_train.pack(padx=10, pady=10)

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tabs Pruebas en vivo ------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.btn_run = ctk.CTkButton(self.tabview.tab('Prueba Turtle'), text='Ejecutar', font=('aptos', 30), width=350, height=150, command=self.turnon)
        self.btn_run.pack(padx=10, pady=10)

        self.btn_stop = ctk.CTkButton(self.tabview.tab('Prueba Turtle'), text='Detener', font=('aptos', 30), width=350, height=150, command=self.turnoff)
        self.btn_stop.pack(padx=10, pady=10)

        self.btn_runW = ctk.CTkButton(self.tabview.tab('Prueba Webots'), text='Ejecutar', font=('aptos', 30), width=350, height=150, command=self.turnonW)
        self.btn_runW.pack(padx=10, pady=10)

        self.btn_stopW = ctk.CTkButton(self.tabview.tab('Prueba Webots'), text='Detener', font=('aptos', 30), width=350, height=150, command=self.turnoffW)
        self.btn_stopW.pack(padx=10, pady=10)

        self.btn_runE = ctk.CTkButton(self.tabview.tab('Prueba ESP32/POLOLU'), text='Ejecutar', font=('aptos', 30), width=350, height=150, command=self.turnonE)
        self.btn_runE.pack(padx=10, pady=10)

        self.btn_stopE = ctk.CTkButton(self.tabview.tab('Prueba ESP32/POLOLU'), text='Detener', font=('aptos', 30), width=350, height=150, command=self.turnoffE)
        self.btn_stopE.pack(padx=10, pady=10)

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración final  -----------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funciones de botones para fotos ------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    def actL(self):
        self.feed.showIMG()
        self.feed.takePHOTO()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funciones para manejo de datos  ------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def reset(self):
        self.feed.resetMaster()
        messagebox.showinfo(message='Listo')
    def erase(self):
        self.feed.eraseSERIES()
        messagebox.showinfo(message='Listo')
    def trainM(self):
        self.feed.loadD()
        self.feed.eraseSERIES()
        self.train1.TrainModel()
        messagebox.showinfo(message='Listo')


    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funcion para prueba en vivo  ---------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def turnon(self):
        self.use_m.on()

    def turnoff(self):
        self.use_m.stop()

    def turnonW(self):
        self.use_w.on()

    def turnoffW(self):
        self.use_w.stop()

    def turnonE(self):
        self.use_bt.on()

    def turnoffE(self):
        self.use_bt.stop()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funcion de cerrardo  -----------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def on_closing(self):
        self.feed.eraseSERIES()
        self.root.destroy()


pGUI()
