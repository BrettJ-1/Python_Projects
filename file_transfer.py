import tkinter as tk #importing modules
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
import datetime

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer") #Created title

        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command = self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady =(30, 0))
        self.source_dir = Entry(self.master, width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady =(30, 0))

        self.destDir_btn = Button (self.master, text="Select Destination", width = 20, command = self.destDir) #Creating button layouts
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady =(15, 10))
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady =(15, 10))

        self.transfer_btn = Button(self.master, text="Transfer Files", width=20, command= self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady= (0, 15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady= (0, 15))

    def sourceDir (self):
        selectSourceDir = tkinter.filedialog.askdirectory() #Allows user to insert Source Directory
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)
        self.source_dir.insert(0, selectSourceDir)

    def destDir (self):
        selectDestDir= tkinter.filedialog.askdirectory() #Allows user to insert Destination Directory
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles (self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for i in source_files:
            shutil.move (source + '/Documents/GitHub/Python_Projects/Customer Source' + i, destination) #Moves files from Customer Source to Cusomer Destination
            print (i + ' was successfully transferred.')   

        current_time = datetime.datetime.now()
        file_path = '/Documents/GitHub/Python_Projects/Customer Destination'
        file_modification_time = os.path.getmtime(file_path)
        time_variation = current_time - file_modification_time
        if time_variation < 86400:
            print(i + ' is considered a new file and was successfully transferred') #Utilized getmtime to detect files that have been modified within 24 hours

    def exit_program (self): #Exits the program
        root. destroy ()
        
if __name__ == "__main__": #Utilizing tkinter
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



