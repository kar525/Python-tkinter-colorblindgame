#1.เลขที่ 7 เลขทะเบียน 6203684300 2.ในปัจจุบันฟิลเตอร์แยกสีเป็นที่นิยมเล่นกัน นักศึกษาจึงอยากจำลองออกมาในรูปแบบ GUI python program 3.program นี้ ใช้ widget 1.button 2.toplevel 3.label 4.messagebox
import random as rn
import tkinter as tk
from tkinter import messagebox
from tkinter import font
class colorgame(tk.Frame):
   C = 50
   N1 = 205
   Score = 0
   def __init__(self, master=None):
      super().__init__(master)
      self.master = master
      self.pack()
      self.create_widgets()
   def rgb_to_hex(self,r, g, b):
      return '#{:02x}{:02x}{:02x}'.format(r, g, b)
   def you_lose(self):
      self.master.destroy()
      messagebox.showerror("You lose","Your score: "+str(self.Score-1)) #messagebox
      AA.config(state=tk.NORMAL)
      BB.config(state=tk.NORMAL)
   def create_widgets(self):
      A = [rn.randrange(0,255),rn.randrange(0,255),rn.randrange(0,255)]
      B = rn.randrange(1,9)
      self.Score += 1
      self.Scorelabel = tk.Label(self, text="Score: "+str(self.Score-1),font = ('Helvetica', 17)) #Lebel
      self.Scorelabel.grid(row = 13, column=2)
      for i in range (1,10):
         if i <= 3:
            if i == B:
               if A[1] <= self.N1:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]+self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]+self.C,A[2]),height="3",width="6").grid(row=1,column=i,padx = 20,pady = 20)
               else:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]-self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]-self.C,A[2]),height="3",width="6").grid(row=1,column=i,padx = 20,pady = 20)
            else:
               tk.Button(self,command=self.you_lose,bg=self.rgb_to_hex(A[0],A[1],A[2]),activebackground = self.rgb_to_hex(A[0],A[1],A[2]),height="3",width="6").grid(row=1,column=i,padx = 20,pady = 20)
         elif i <= 6:
            if i == B:
               if A[1] <= self.N1:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]+self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]+self.C,A[2]),height="3",width="6").grid(row=2,column=i-3,padx = 20,pady = 20)
               else:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]-self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]-self.C,A[2]),height="3",width="6").grid(row=2,column=i-3,padx = 20,pady = 20)
            else:
               tk.Button(self,command=self.you_lose,bg=self.rgb_to_hex(A[0],A[1],A[2]),activebackground = self.rgb_to_hex(A[0],A[1],A[2]),height="3",width="6").grid(row=2,column=i-3,padx = 20,pady = 20)
         else:
            if i == B:
               if A[1] <= self.N1:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]+self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]+self.C,A[2]),height="3",width="6").grid(row=3,column=i-6,padx = 20,pady = 20)
               else:
                  tk.Button(self,command=self.create_widgets,bg=self.rgb_to_hex(A[0],A[1]-self.C,A[2]),activebackground = self.rgb_to_hex(A[0],A[1]-self.C,A[2]),height="3",width="6").grid(row=3,column=i-6,padx = 20,pady = 20)
            else:
               tk.Button(self,command=self.you_lose,bg=self.rgb_to_hex(A[0],A[1],A[2]),activebackground = self.rgb_to_hex(A[0],A[1],A[2]),height="3",width="6").grid(row=3,column=i-6,padx = 20,pady = 20)
         
class normalcolorgame(colorgame):
   C = 30
   N1 = 225
class hardcolorgame(colorgame):
   C = 10
   N1 = 245

gm = 1

def opengame():
   def closebaseL():
      base.destroy()
      try:
         L.destroy()
      except:
         print ("Game close")
   def open():
      def enable_button():
         L.destroy()
         AA.config(state=tk.NORMAL)  # เปิดการใช้งาน ปุ่ม Play และ game mode
         BB.config(state=tk.NORMAL)
      return enable_button()
   base.protocol("WM_DELETE_WINDOW", closebaseL)
   AA.config(state=tk.DISABLED)
   BB.config(state=tk.DISABLED)
   L = tk.Tk()
   L.geometry("350x450")
   L.protocol("WM_DELETE_WINDOW",open)
   if gm == 1:
      L.title("Color Game: Easy mode")
      app = colorgame(master=L)
      app.mainloop()
   elif gm == 2:
      L.title("Color Game: Normal mode")
      app = normalcolorgame(master=L)
      app.mainloop()
   else:
      L.title("Color Game: Hard mode")
      app = hardcolorgame(master=L)
      app.mainloop()

def gamemode():
   def easy():
      global gm
      gm = 1
      return gm
   def normal():
      global gm
      gm = 2
      return gm
   def hard():
      global gm
      gm = 3
      return gm
   def on_toplevel_close():
      def enable_button():
         Top1.destroy()  # ปิดtoplevel
         AA.config(state=tk.NORMAL)  # เปิดการใช้งาน ปุ่ม Play และ game mode
         BB.config(state=tk.NORMAL)
      return enable_button
   Top1 = tk.Toplevel(base) #Toplevel
   Top1.title("Game mode")
   Top1.geometry("250x250")
   Top1.config(bg="#07D093")

   B1 = tk.Button(Top1, text="Easy", command=easy,height="2",width="9")
   B2 = tk.Button(Top1, text="Normal", command=normal,height="2",width="9")
   B3 = tk.Button(Top1, text="Hard", command=hard,height="2",width="9")

   B1.place(x=100, y=50)
   B2.place(x=100, y=100)
   B3.place(x=100, y=150)
   AA.config(state=tk.DISABLED) #เมื่อเรียกใช้ฟังค์ชั่น gamemode ปิดการใช้งาน ปุ่ม Play และ game mode
   BB.config(state=tk.DISABLED)
   Top1.protocol("WM_DELETE_WINDOW", on_toplevel_close()) #เมื่อปิด Top level เรียกฟังค์ชั่น on_toplevel_close
base = tk.Tk()
base.geometry("400x400")
base.config(bg='#00ABFF')
AA = tk.Button(base,command=opengame,activebackground = "yellow",text="Play",height="3",width="12") #Button
BB = tk.Button(base,command=gamemode,activebackground = "yellow",text="Game mode",height="3",width="12")
try:
   Cat1 = tk.PhotoImage(file="Bacat.png")
   Cat2 = tk.PhotoImage(file="Ocat.png")
   P1 = tk.Label(base,image=Cat1)
   P2 = tk.Label(base,image=Cat2)
   P1.config(bg="#00ABFF")
   P2.config(bg="#00ABFF")
   P1.place(x=0, y= 290)
   P2.place(x=300, y= 0)
except:
   print("Image not found") 
AA.place(x=150, y=75)
BB.place(x=150, y=175)
base.title("Main")
base.mainloop()

#เมื่อกดปุ่มplay จะสามารถเข้าไปเล่นเกมแยกสีได้ และ ปุ่มgame mode จะพาเข้าไปหน้า toplevel เพื่อเลือกระดับความยากของเกมเลือกสี


