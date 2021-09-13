import tkinter as tk
import numpy as np

class CriticalPressureCalculator:
    
    def __init__(self):
        window = Tk()
        window.title("Critical Pressure Threshold Calculator for Area of Review Estimation")
        
        #input values
        Label(window, text = "Measured depth to base of lowermost USDW (m):").grid(row = 1, column = 1, sticky = W, pady = (20, 0))
        Label(window, text = "Pressure at the base of the lowermost USDW (Pa):").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Measured depth to the injection zone (m):").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Pressure at the top of the injection zone (Pa):").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Fluid density within the injection zone (kg/m3):").grid(row = 5, column = 1, sticky = W)
        
        #blank space between inputs and calculation result
        Label(window, text = "").grid(row = 6, column = 1, sticky = W)
                
        #output value
        Label(window, text = "Critical Pressure: ").grid(row = 8, column = 1, stick = W)
        
        #initialize variables for inputs
        self.input1 = StringVar()
        self.input2 = StringVar()
        self.input3 = StringVar()
        self.input4 = StringVar()
        self.input5 = StringVar()
       
        #variable for output
        self.critp = StringVar()
        
        #input entry boxes
        Entry(window, textvariable = self.input1, justify = RIGHT).grid(row = 1, column = 2, pady = (20,0))
        Entry(window, textvariable = self.input2, justify = RIGHT).grid(row = 2, column = 2)
        Entry(window, textvariable = self.input3, justify = RIGHT).grid(row = 3, column = 2)
        Entry(window, textvariable = self.input4, justify = RIGHT).grid(row = 4, column = 2)
        Entry(window, textvariable = self.input5, justify = RIGHT).grid(row = 5, column = 2)
        
        #output box
        Label(window, textvariable = self.critp).grid(row = 8, column = 2)
        
        Button(window, text = "Calculate Critical Pressure", command = self.calcPressure).grid(row = 7, column = 2, padx = (0, 20), pady = 5)
        
        #render form
        window.mainloop()
        
        #calculate critical pressure threshold
    def calcPressure(self):
        input1 = float(self.input1.get())
        input2 = float(self.input2.get())
        input3 = float(self.input3.get())
        input4 = float(self.input4.get())
        input5 = float(self.input5.get())
        
        #equation 1 Calcuation
        critp = (input2 + (input5 * 9.8067) * (input3 - input1) - input4)
        
        self.critp.set(format(critp,"8,.2f"))
        
CriticalPressureCalculator()