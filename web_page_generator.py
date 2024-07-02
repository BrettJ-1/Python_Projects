import tkinter as tk
from tkinter import * #importing modules
from tkinter import ttk 
import webbrowser

class ParentWindow (Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML) #Sets the button up named "Default HTML Page"
        self.btn.grid(padx=(10, 10), pady=(10, 10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>" #Creates format for basic website
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def get_data():
        win = Tk()
        label= Label(win, text="", font=('Helvetica 13')) #Returns input data from user
        label.pack()
        entry = Entry(win, width= 42)
        entry.place(relx= .5, rely= .5, anchor= CENTER)
        label.config(text= entry.get(), font= ('Helvetica 13'))

    def enter_input():
        win = Tk()
        ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER) #Creates button for input data

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root) #Utilizing tkinter
    root.mainloop()        
