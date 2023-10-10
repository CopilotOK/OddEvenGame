import tkinter 
from tkinter import ttk
import time

def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

def startgame():
   startwindow = tkinter.Tk()
   startwindow.title("Loading Game...")
   
   center(startwindow) 
   startwindow.geometry("500x100")
   startwindow.configure(bg='black')


   bar = ttk.Progressbar(startwindow, orient="horizontal", length=300, )
   bar.pack(anchor="center", ipady=0.5, pady=10)

   startLabel = tkinter.Label(startwindow, foreground='white', text="Starting game..", background='black')
   startLabel.pack(anchor='s')

   b = 100
   a = 1

   while a<b:
         
         time.sleep(0.0001)
         bar['value']+=1
         a+=1
         startwindow.update_idletasks()
         
   startwindow.destroy()
   return 
   startwindow.mainloop()