from tkinter import *

from random import randint
import PySimpleGUI as sg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk

sg.theme('Dark Green 7')

layout = [ [sg.Txt('Enter values to calculate')],
           [sg.In(size=(8,1), key='-NUMERATOR-')],
           [sg.Txt('_'  * 10)],
           [sg.In(size=(8,1), key='-DENOMINATAOR-')],
           [sg.Txt(size=(8,1), key='-OUTPUT-')  ],
           [sg.Button('Calculate', bind_return_key=True)]]

window = sg.Window('Math', layout)

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:
        try:
            numerator = float(values['-NUMERATOR-'])
            denominator = float(values['-DENOMINATAOR-'])
            calc = numerator/denominator
        except:
            calc = 'Invalid'

        window['-OUTPUT-'].update(calc)
    else:
        break