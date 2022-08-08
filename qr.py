import pyqrcode

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from io import BytesIO
import PIL.Image

from PIL import Image, ImageTk

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import matplotlib.pyplot as plt


class Ventana:
    def __init__(self, master):
        self.master = master
        master.title("Generador QR")

        self.etiqueta = Label(master, text="Escribe información del QR")
        self.etiqueta.pack()

        self.botonQr = Button(master, text="Crear", command=self.crear)
        self.botonQr.pack()


        self.textURL = Entry(master, text="Crear")
        self.textURL.pack()



    def crear(self):
        titl = self.textURL.get()
        url = pyqrcode.create(self.textURL.get())

        #Crear SVG
        url.svg("qr.svg", scale=1)
        print("QR created. qr.svg")

        #Print etiqueta contenido QR
        self.etiqueta = Label(text=self.textURL.get())
        self.etiqueta.pack()

        #Print SVG

        drawing = svg2rlg("qr.svg")
        renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
        img = Image.open('temp.png')
        plt.figure("qr_"+titl)
        plt.imshow(img)

        #img.show()
        plt.show()


root = Tk()
root.geometry('200x200')
miVentana = Ventana(root)
root.mainloop()



