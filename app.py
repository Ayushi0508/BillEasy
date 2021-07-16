import tkinter
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Billing System")
        self.root.geometry("1350*750+0+0")
        self.root.config(background="powder blue")

        ABC=Frame(self.root,bg="powder blue",bd=20,relief=RIDGE)
        ABC.grid()
        ABC1=Frame(ABC,bd=14,width=1350,height=100,padx=10,bg="powder blue",relief=RIDGE)
        ABC1.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC2=Frame(ABC,bd=14,width=450,height=488,padx=10,bg="cadet blue",relief=RIDGE)
        ABC2.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC3=Frame(ABC,bd=14,width=450,height=488,padx=10,bg="powder blue",relief=RIDGE)
        ABC3.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC4=Frame(ABC,bd=14,width=460,height=488,padx=10,bg="cadet blue",relief=RIDGE)
        ABC4.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC5=Frame(ABC4,bd=14,width=370,height=340,padx=10,bg="cadet blue",relief=RIDGE)
        ABC5.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC6=Frame(ABC4,bd=14,width=370,height=120,padx=10,bg="cadet blue",relief=RIDGE)
        ABC6.grid(row=0,column=0,columnspan=4,sticky=W)


if __name__=='__main__':
    root=Tk()
    application=Customer(root)
    root.mainloop()
