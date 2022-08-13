from Inverse import *
from Plot import *
import tkinter as tk
from tkinter import ttk


def main():
    window = Tk()
    window.geometry("1200x900")
    window.title("Matrix")
    
    tabControl = ttk.Notebook(window)
    
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    
    tabControl.add(tab2, text="Inverse Matrix")
    tabControl.add(tab3, text="Data Visualization")
    tabControl.pack(expand = 1, fill="both")
    dot2(tab2)
    dot3(tab3)
    window.mainloop()
    
if __name__ == "__main__":
    main()