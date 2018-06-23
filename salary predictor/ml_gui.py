import tkinter as tk
from tkinter import ttk
from project import prediction
class public_data(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.geometry(self,'400x500')
        tk.Tk.wm_title(self,'SALARY PREDICTOR')
        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        
        self.frames={}
        
        frame = Startpage(container, self)
        self.frames[Startpage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        frame = Prediction(container,self)
        self.frames[Prediction]=frame
        frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame(Startpage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Startpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="WELCOME TO SALARY\nPREDICTION SYSTEM",font=('arail',20))
        label.pack(padx=20,pady=20)
        
        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(Prediction))
        button.pack()
class Prediction(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #-----------------------------------
        self.age=float()
        self.w_hrs=int()
        self.w_cls=str()
        self.ocp=str()
        self.edu=str()
        self.ctry=str()
        def get_value():
            a=str(prediction(self.age,self.w_hrs,self.w_cls,self.edu,self.ocp,self.ctry))
            ans_label.configure(text=a)
            #configure(self,text=self.a)
        #-----------------------------------
        label = ttk.Label(self,text='PREDICTION PANEL',)
        label.pack(padx=20,pady=20)
        age_label=ttk.Label(self, text="Age:",font=('arail',10))
        age_label.place(x=100,y=60)
        age_entry=ttk.Entry(self,textvariable=self.age)
        age_entry.place(x=190,y=60)
        
        w_hrs_label=ttk.Label(self, text="Working hour:",font=('arail',10))
        w_hrs_label.place(x=100,y=100)
        w_hrs_entry=ttk.Entry(self,textvariable=self.w_hrs)
        w_hrs_entry.place(x=190,y=100)
        
        ocp_label=ttk.Label(self, text="Occupation:",font=('arail',10))
        ocp_label.place(x=100,y=140)
        ocp_entry=ttk.Entry(self,textvariable=self.ocp)
        ocp_entry.place(x=190,y=140)
        
        ctry_label=ttk.Label(self, text="Country:",font=('arail',10))
        ctry_label.place(x=100,y=180)
        ctry_entry=ttk.Entry(self,textvariable=self.ctry)
        ctry_entry.place(x=190,y=180)
        
        w_cls_label=ttk.Label(self, text="Working class:",font=('arail',10))
        w_cls_label.place(x=100,y=220)
        w_cls_entry=ttk.Entry(self,textvariable=self.w_cls)
        w_cls_entry.place(x=190,y=220)
        
        edu_label=ttk.Label(self, text="Education:",font=('arail',10))
        edu_label.place(x=100,y=260)
        edu_entry=ttk.Entry(self,textvariable=self.edu)
        edu_entry.place(x=190,y=260)
        
        sub_btn=ttk.Button(self,text='submit',command=get_value)
        sub_btn.place(x=160,y=300)
        
        
        ans_label=tk.Label(self,text='',font=('arail',15,'bold'))
        ans_label.place(x=90,y=340)
        
root=public_data()
root.mainloop()
    